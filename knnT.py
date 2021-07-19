import os
import operator

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def img_2_txt():
    for i in range(0, 10):
        img = Image.open(r'.\handwritten\%s.png' % i)
        # 将图片像素更改为32X32
        img = img.resize((32, 32))
        # 将彩色图片变为黑白图片
        img = img.convert('L')
        # 保存
        path = r'.\handwritten\%s_new.jpg' % i
        img.save(path)

    for i in range(0, 10):
        fb = open(r'.\hand_written\%s_handwritten.txt' % i, 'w')
        new_img = Image.open(r'.\handwritten\%s_new.jpg' % i)
        # 读取图片的宽和高
        width, height = new_img.size
        for i2 in range(height):
            for j in range(width):
                # 获取像素点
                color = new_img.getpixel((j, i2))
                # 像素点较高的为图片中的白色
                if color > 170:
                    fb.write('0')
                else:
                    fb.write('1')
            fb.write('\n')
        fb.close()


# 处理文本文件
def img_2_vector(file):
    # 创建一个1*1024的一维零矩阵
    the_matrix = np.zeros((1, 1024))
    fb = open(file)
    for i in range(32):
        # 逐行读取
        line_str = fb.readline()
        for j in range(32):
            # 将32*32=1024个元素赋值给一维零矩阵
            the_matrix[0, 32 * i + j] = int(line_str[j])
    return the_matrix


# 将txt文件转换为 png 图片
def file_2_img(filename, target):
    fr = open(filename)
    name = filename.split('/')[-1][:-4]
    print(name)
    image = Image.new('L', (32, 32))
    for i in range(32):
        line_str = fr.readline()
        for j in range(32):
            color_value = int(line_str[j])
            if color_value == 1:
                color_value = 255
            image.putpixe((j, i), int(color_value))
            image.save(target + '/' + name + '.png')


# 生成图片
def gen_img(filename, target):
    file_list = os.listdir(filename)
    m = len(file_list)
    if not os.path.exists(target):
        os.mkdir(target)

    for i in range(m):
        file_2_img(filename + file_list[i], target)


# KNN分类器
def classifier(test_data, train_data, label, k):
    size = train_data.shape[0]
    # 将测试数据每一行复制size次减去训练数据，横向复制size次，纵向复制1次
    the_matrix = np.tile(test_data, (size, 1)) - train_data
    # 将相减得到的结果平方
    sq_the_matrix = the_matrix ** 2
    # 平方加和，axis = 1 代表横向
    all_the_matrix = sq_the_matrix.sum(axis=1)
    # 结果开根号得到最终距离
    distance = all_the_matrix ** 0.5
    # 将距离由小到大排序，给出结果为索引
    sort_distance = distance.argsort()
    dis_dict = {}
    # 取到前k个
    for i in range(k):
        # 获取前K个标签
        the_label = label[sort_distance[i]]
        # 将标签的key和value传入字典
        dis_dict[the_label] = dis_dict.get(the_label, 0) + 1
    # 将字典按value值的大小排序，由大到小，即在K范围内，筛选出现次数最多几个标签
    sort_count = sorted(dis_dict.items(), key=operator.itemgetter(1), reverse=True)
    # 返回出现次数最多的标签
    return sort_count[0][0]


def hand_writing_class_test(k):
    labels = []
    # listdir方法是返回一个文件夹中包含的文件
    train_data = os.listdir('trainingDigits')
    # 获取该文件夹中文件的个数
    m_train = len(train_data)
    # 生成一个列数为train_matrix，行为1024的零矩阵
    train_matrix = np.zeros((m_train, 1024))
    for i in range(m_train):
        file_name_str = train_data[i]
        file_str = file_name_str.split('.')[0]
        # 切割出训练集中每个数据的真实标签
        file_num = int(file_str.split('_')[0])
        labels.append(file_num)
        # 将所有训练数据集中的数据都传入到train_matrix中
        train_matrix[i, :] = img_2_vector('trainingDigits/%s' % file_name_str)

    error = []
    test_matrix = os.listdir('testDigits')
    correct, error_count = 0.0, 0.0
    m_test = len(test_matrix)
    for i in range(m_test):
        file_name_str = test_matrix[i]
        file_str = file_name_str.split('.')[0]
        # 测试数据集每个数据的真实结果
        file_num = int(file_str.split('_')[0])
        vector_test = img_2_vector('testDigits/%s' % file_name_str)
        classify_result = classifier(vector_test, train_matrix, labels, k)
        print('预测结果：%s\t真实结果：%s' % (classify_result, file_num))
        if classify_result == file_num:
            correct += 1.0
        else:
            error_count += 1.0
            error.append((file_name_str, classify_result))
    print("正确率:{:.2f}%".format(correct / float(m_test) * 100))
    print('error', len(error), error)
    return error_count


# 测试不同的k值，识别的效果如何
def select_k():
    x, y = list(), list()
    for i in range(1, 5):
        x.append(i)
        y.append(int(hand_writing_class_test(i)))

    plt.plot(x, y)

    os.system('say completed!')
    plt.show()

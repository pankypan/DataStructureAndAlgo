# utf-8


class SortedArray:
    """大小固定的有序数组"""
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * self._capacity

    def get(self, index):
        if index >= self._size - 1:
            return False
        return self._data[index]

    def add(self, elem):
        # 首元素添加
        if self._size == 0:
            self._data[0] = elem
            self._size += 1
            return
        # 数组已满
        if self._size == self._capacity:
            print('This basicDS03_array is full!')
            return
        # 倒序遍历数组，移动后面的元素，直到找到插入位置
        for i in range(self._size - 1, -1, -1):
            if elem < self._data[i]:
                self._data[i + 1] = self._data[i]
            else:
                break
        # 找到位置进行插入，更新size
        self._data[i + 1] = elem
        self._size += 1

    def delete(self, index: int):
        if index < 0 or index >= self._size - 1:
            print('Invalid index')
            return
        for i in range(index, self._size, 1):
            self._data[i] = self._data[i+1]
        self._size -= 1

    def print(self):
        array = []
        for i in range(self._size):
            array.append(self._data[i])
        print(f'sorted_array {array}')


class DynamicArray:
    """支持动态扩容的数组"""
    def __init__(self, capacity=10):
        """
        构造函数
        """
        self._capacity = capacity  # 数组最大容量
        self._size = 0  # 数组已使用的大小
        self._data = [None] * self._capacity  # 初始元素

    def insert(self, index, elem):
        """
        注意数组占用的是一段连续的内存空间，所以在添加元素之前，需要将后面的元素都向后挪一个位置，
        而且要注意要先从尾部开始挪，防止元素之间的覆盖
        """
        # 1 index有效性判断
        if index < 0 or index > self._size:
            print('index不合法')
            return

        # 2 判断容量是否已满(已满扩容)
        # 默认扩容为原来容量的2倍
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        # 3 在指定位置插入元素
        # 先将index之后的元素全部依次后移一位
        for i in range(self._size - 1, index - 1, -1):
            self._data[i+1] = self._data[i]  # 元素后移
        self._data[index] = elem

        # 4 更新size
        self._size += 1

    def _resize(self, new_capacity):
        """
        扩容方法
        """
        # 1 新建一个大容量数组
        new_arr = DynamicArray(new_capacity)

        # 2 将现在self._data的元素逐个拷贝到新数组
        for i in range(self._size):
            new_arr.insert(i, self._data[i])

        # 3 更新变量
        self._capacity = new_capacity
        self._data = new_arr._data

    def print(self):
        """
        打印数组
        """
        for i in range(self._size):
            print(self._data[i], end='\t')


def test_array():
    s_array = SortedArray(10)
    s_array.print()
    for i in range(7):
        s_array.add(i+1)
    s_array.print()
    s_array.add(2.8)
    s_array.print()
    s_array.delete(2)
    s_array.print()


if __name__ == "__main__":
    test_array()

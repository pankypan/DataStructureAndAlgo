

class SNode:
    """跳跃表节点的类"""
    def __init__(self, key=None, value=None):
        # 键
        self.key = key
        # index表示数组中最末的元素
        self.maxIndex = -1
        # link使用一个数组  存放全部下节点的索引  link[i]表示第i层的索引
        self.link = []
        self.value = value

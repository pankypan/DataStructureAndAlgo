# utf-8
"""
包括 单链表，循环链表，双向链表
"""


class Node(object):
    """链表结构的Node节点"""

    def __init__(self, data, next_node=None):
        """
        Node节点的初始化方法.
        :param data: 存储的数据
        :param next_node: 下一个Node节点的引用地址
        """
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        """
        Node节点存储数据的获取.
        :return:当前Node节点存储的数据
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        Node节点存储数据的设置方法.
        :param data:新的存储数据
        :return:
        """
        self.__data = data

    @property
    def next_node(self):
        """
        获取Node节点的next指针值.
        :return:next指针数据
        """
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        """
        Node节点next指针的修改方法.
        :param next_node: 新的下一个Node节点的引用
        :return:
        """
        self.__next = next_node


class SingleCycleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        # 前驱区
        self.prev = None
        # 后继区
        self.next = None


class SingleLinkedList(object):
    """单向链表"""

    def __init__(self, head=None):
        """单向链表的初始化方法"""
        self.__head = head

    def find_by_value(self, value):
        node = self.__head
        while node is not None and node.data != value:
            node = node.next_node
        return node

    def find_by_index(self, index):
        node = self.__head
        pos = 0
        while node is not None and pos != index:
            node = node.next_node
            pos += 1
        return node

    def insert_to_head(self, value):
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    @staticmethod
    def insert_after(node, value):
        if node is None:
            return
        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_before(self, node, value):
        """在链表的某个指定Node节点之前插入一个存储value数据的Node节点.
            参数:
                node:指定的一个Node节点
                value:将要存储在新的Node节点中的数据
            """
        if (node is None) or (self.__head is None):  # 如果指定在一个空节点之前或者空链表之前插入数据节点，则什么都不做
            return

        if node == self.__head:  # 如果是在链表头之前插入数据节点，则直接插入
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定插入的Node节点，则该标记量设置为True
        while pro.next_node != node:  # 寻找指定Node之前的一个Node
            if pro.next_node is None:  # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node

    def delete_by_node(self, node):
        """在链表中删除指定Node的节点.
                参数:
                    node:指定的Node节点
                """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return

        if node == self.__head:  # 如果指定删除的Node节点是链表的头节点
            self.__head = node.next_node
            return

        pro = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定删除的Node节点，则该标记量设置为True
        while pro.next_node != node:
            if pro.next_node is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到指定删除的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_by_value(self, value):
        """在链表中删除指定存储数据的Node节点.
                参数:
                    value:指定的存储数据
                """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return

        if self.__head.data == value:  # 如果链表的头Node节点就是指定删除的Node节点
            self.__head = self.__head.next_node

        pro = self.__head
        node = self.__head.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到执行Value值的Node节点
                not_found = True
                break
            else:
                pro = node
                node = node.next_node
        if not_found is False:
            pro.next_node = node.next_node


class SingleCycleLinkedList(object):
    """
    单向循环链表：单向循环链表相对于单链表，
    区别在于链表中最后一个节点的next区域不在指向None，
    而是指向链表的头节点。
    """

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        if self.is_empty():
            return 0

        count = 1
        # cur: 游标 用来移动遍历节点
        cur = self.__head

        while cur.next != self.__head:
            count += 1
            cur = cur.next

        return count

    def print(self):
        """遍历整个链表"""
        if self.is_empty():
            return

        cur = self.__head
        while cur.next != self.__head:
            print(cur.val, end=" ")
            cur = cur.next
        print(cur.val)

    def add(self, item):
        """在头部添加元素"""
        node = SingleCycleNode(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """在尾部添加元素"""
        node = SingleCycleNode(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """在指定位置添加元素"""

        if pos < 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = SingleCycleNode(item)
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除某个元素"""

        if self.is_empty():
            return

        pre = None
        cur = self.__head

        while cur.next != self.__head:
            if cur.val == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    # 若是头节点，得先找到尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = cur.next
                else:
                    pre.next = cur.next
                return item
            else:
                pre = cur
                cur = cur.next

        # 退出循环，指向尾节点
        if cur.val == item:
            if cur.next == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = self.__head
            return item

        return None

    def search(self, item):
        """查找节点是否存在"""

        if self.is_empty():
            return -1

        count = 0
        cur = self.__head
        while cur.next != self.__head:
            if cur.val == item:
                return count
            cur = cur.next
            count += 1

        if cur.val == item:
            return count

        return -1


class DoubleLinkedList(object):
    def __init__(self, head=None):
        self.__head = head

    def is_empty(self):
        return self.__head is None

    def __len__(self):
        count = 0
        cur = self.__head
        while cur:
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        cur = self.__head
        while cur:
            print(cur.value)
            cur = cur.next

    def add(self, value):
        node = DoubleLinkedListNode(value)
        if self.is_empty():
            self.__head = node
            return True

        node.next = self.__head   # 待插入节点的后继区指向原头节点
        self.__head.prev = node  # 原头节点的前驱区指向待插入节点

        self.__head = node

    def append(self, value):
        new_node = DoubleLinkedListNode(value)
        if self.is_empty():
            self.__head = new_node
            return True
        cur = self.__head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos > len(self) - 1:
            self.append(value)
        else:
            # 单向链表中为了在特定位置插入，要先在链表中找到待插入位置和其前一个位置
            # 双向链表中就不需要两个游标了（当然单向链表中一个游标也是可以只找前一个位置）
            new_node = DoubleLinkedListNode(value)
            count = 0
            cur = self.__head
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 此时的游标指向pos的前一个位置
            # 这里的相互指向需尤为注意，有多种实现，需细细分析
            new_node.next = cur.next
            cur.next.prev = new_node
            new_node.prev = cur
            cur.next = new_node

    def search(self, value):
        cur = self.__head
        while cur:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, value):
        if self.is_empty():
            return
        cur = self.__head
        while cur:
            if cur.value == value:
                if cur == self.__head:
                    self.__head = cur.next
                    # 处理链表只有一个节点的特殊情况
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 处理待删除节点是最后一个情况
                    if cur.next:
                        cur.next.prev = cur.prev
                return
            else:
                cur = cur.next

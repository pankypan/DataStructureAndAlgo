"""
实现：
    1) 基于数组的队列
    2) 基于数组的动态队列(动态扩容)
    3) 基于链表的队列
    4) 循环队列
"""

from typing import Optional
from itertools import chain


class Node:
    def __init__(self, data: str, next_node=None):
        self.data = data
        self._next = next_node


class ArrayQueue(object):
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:  # 数组容量限制
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):  # 移动覆盖
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0

        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head : self._tail])


class DynamicArrayQueue:
    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0: return False

            self._items[0: self._tail - self._head] = self._items[self._head: self._tail]
            self._tail -= self._head
            self._head = 0

        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head:self._tail])


class LinkedQueue:
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def enqueue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return value

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return "->".join(value for value in values)


class CircularQueue:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            return False

        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head: self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == "__main__":
    # 测试动态数组队列
    q = DynamicArrayQueue(10)
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)

    # 测试循环队列
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    print(q)

    # 测试链表队列
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)
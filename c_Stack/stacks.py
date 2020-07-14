# utf-8
"""
Stack based on linked list
"""


class Node:
    def __init__(self, data, node_obj=None):
        self.data = data
        self.next = node_obj


class LinkedStack(object):
    def __init__(self):
        self._top: Node = Node(None)

    def push(self, value):
        if isinstance(self._top, Node) and self._top.data is None:
            self._top.data = value
            return
        new_top = Node(value)
        new_top.next = self._top
        self._top = new_top

    def pop(self):
        if self._top:
            value = self._top.data
            self._top = self._top.next
            return value

    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current.data)
            current = current.next
        return " ".join(f"{num}]" for num in nums)

    def is_empty(self):
        return not self._top


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)

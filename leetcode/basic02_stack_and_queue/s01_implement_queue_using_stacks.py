"""
https://leetcode-cn.com/problems/implement-queue-using-stacks/
leetcode 232 easy
"""
from basic02_stack_and_queue.my_stacks import Stack


class MyQueue:
    """核心：使用两个栈，分别主要用于入队、出队"""
    def __init__(self):
        self.s1 = Stack()  # 用于入队
        self.s2 = Stack()  # 用于出队

    def moves_items(self):
        """pop all items form s1 and push them to s2"""
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        if self.s2.is_empty():
            self.moves_items()
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2.is_empty():
            self.moves_items()
        return self.s2.peek()

    def empty(self) -> bool:
        return self.s1.is_empty() and self.s2.is_empty()


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())

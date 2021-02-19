# https://leetcode-cn.com/problems/implement-stack-using-queues/
from basic02_stack_and_queue.my_queues import Queue


class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.push(x)

    def pop(self) -> int:
        top = self.q.get_rear()
        if not top:
            return top
        while self.q.get_front() != top:
            self.q.push(self.q.pop())
        return self.q.pop()

    def top(self) -> int:
        return self.q.get_rear()

    def empty(self) -> bool:
        return self.q.is_empty()


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

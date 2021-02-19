# https://leetcode-cn.com/problems/min-stack/
from basic02_stack_and_queue.my_stacks import Stack


class MinStack:
    def __init__(self):
        self._stack = Stack()
        self._min_stack = Stack()  # 使用辅助栈，来记录当前最小值

    def push(self, x: int) -> None:
        self._stack.push(x)

        # min_stack push 当前栈最小值
        if self._min_stack.peek() is None:
            self._min_stack.push(x)
        else:
            self._min_stack.push(min(x, self._min_stack.peek()))

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack.peek()

    def getMin(self) -> int:
        return self._min_stack.peek()

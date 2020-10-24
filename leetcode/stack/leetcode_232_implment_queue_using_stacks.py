class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []  # 主栈，接受入队元素
        self.stack_aux = []  # 辅助栈

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return -1
        if not self.stack_aux:
            while self.stack:
                self.stack_aux.append(self.stack.pop())
        return self.stack_aux.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1
        if not self.stack_aux:
            while self.stack:
                self.stack_aux.append(self.stack.pop())
        return self.stack_aux[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if not self.stack_aux and not self.stack else False


if __name__ == '__main__':
    s = MyQueue()
    s.push(1)
    s.push(2)
    print(s.peek())
    print(s.pop())
    print(s.empty())


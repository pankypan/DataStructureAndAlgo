class MinStack:
    """核心：利用辅助栈记录当前栈最小value"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min_stack = []  # 辅助栈

    def push(self, x: int) -> None:
        self.__stack.append(x)

        # 利用辅助栈记录当前栈最小value
        cur_stack_min_data = min(x, self.__min_stack[-1]) if self.__min_stack else x
        self.__min_stack.append(cur_stack_min_data)

    def pop(self) -> None:
        self.__stack.pop()
        self.__min_stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def get_min(self) -> int:
        return self.__min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

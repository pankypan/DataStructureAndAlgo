"""算法面试题"""
from basicDS04_stack_and_queue.my_stacks import Stack


class Solution:
    @staticmethod
    def move_bottom_to_top(s: Stack):
        s.items.append(s.items.pop(0))

    def reverseStack(self, s: Stack) -> Stack:
        # 递归边界
        if s.is_empty() or s.size == 1:
            return s

        # 将底部元素移到顶部
        self.move_bottom_to_top(s)
        # 该栈 pop 出一个元素并记录在 top 中，形成子栈，并递归调用翻转方法
        top = s.pop()
        s = self.reverseStack(s)

        # 翻转后的子栈，push 原来的 top 元素
        s.push(top)
        return s


if __name__ == "__main__":
    solution = Solution()
    stack = Stack()
    for i in range(5):
        stack.push(i)

    stack = solution.reverseStack(stack)
    for i in range(10):
        print(stack.pop())
    pass

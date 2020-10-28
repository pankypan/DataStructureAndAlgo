"""
https://leetcode-cn.com/problems/validate-stack-sequences/
leetcode 946 medium
"""
from basic02_stack_and_queue.my_stacks import Stack


class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        """
        核心：贪心
        将 pushed 队列中的每个数都 push 到栈中，同时检查这个数是不是 popped 序列中下一个要 pop 的值，如果是就把它 pop 出来。
        最后，检查不是所有的该 pop 出来的值都是 pop 出来了。
        """
        stack = Stack()

        j = 0
        for item in pushed:
            stack.push(item)
            # 检查元素，并出栈
            while j < len(popped) and stack.peek() == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


if __name__ == "__main__":
    pass

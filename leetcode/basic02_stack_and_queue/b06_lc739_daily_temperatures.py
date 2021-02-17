"""
https://leetcode-cn.com/problems/daily-temperatures/
leetcode 739 medium
"""
from typing import List

from basic02_stack_and_queue.my_stacks import Stack


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        核心：
            1.单调栈
            2.单调栈记录特殊数组 [val, index]
        :param T:
        :return:
        """
        t_len = len(T)
        res_lis = [0] * t_len
        stack = Stack()  # stack 记录特殊数组 [值, 位置index]

        for i in range(t_len - 1, -1, -1):
            # 1.维护单调栈
            while not stack.is_empty() and T[i] >= stack.peek()[0]:
                stack.pop()

            # 2.利用单调栈
            res_lis[i] = 0 if stack.peek() is None else stack.peek()[1] - i

            # 3.元素 push 进入单调栈
            stack.push([T[i], i])
        return res_lis


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    pass

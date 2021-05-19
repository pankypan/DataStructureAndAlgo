# https://leetcode-cn.com/problems/next-greater-element-i/
from typing import List

from basicDS04_stack_and_queue.my_stacks import Stack


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        核心：
            1.单调栈
            2.利用取模运算(%)获得环形特效，解决环形数组
        """
        monotonous_stack = Stack()
        nums_len = len(nums)
        res_lis = [-1] * nums_len

        # 将 nums2 的所有元素，倒序入单调栈
        for i in range(nums_len * 2 - 1, -1, -1):
            index = i % nums_len
            # 1.维护单调栈
            while not monotonous_stack.is_empty() and nums[index] >= monotonous_stack.peek():
                monotonous_stack.pop()

            # 2.利用栈
            res_lis[index] = monotonous_stack.peek() if monotonous_stack.peek() is not None else -1

            # 3.单调栈入栈
            monotonous_stack.push(nums[index])
        return res_lis


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElements([-1, 0]))
    pass

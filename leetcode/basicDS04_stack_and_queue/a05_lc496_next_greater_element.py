# https://leetcode-cn.com/problems/next-greater-element-i/
from typing import List

from basicDS04_stack_and_queue.my_stacks import Stack


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """核心：单调栈"""
        monotonous_stack = Stack()  # 单调栈,单调递减
        memory_dic = {}

        # 将 nums2 的所有元素，倒序入单调栈
        for i in range(len(nums2) - 1, -1, -1):
            # 1.维护单调栈--[将单调栈中 <= 当前元素(nums2[i])的元素，全部 pop 出去]
            while not monotonous_stack.is_empty() and nums2[i] >= monotonous_stack.peek():
                monotonous_stack.pop()

            # 2.使用单调栈--[根据单调栈的栈顶元素(stack.peek()),获取值]
            memory_dic[nums2[i]] = -1 if monotonous_stack.is_empty() else monotonous_stack.peek()

            # 3.元素入栈
            monotonous_stack.push(nums2[i])
        return [memory_dic.get(item) for item in nums1]

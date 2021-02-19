# https://leetcode-cn.com/problems/maximum-binary-tree/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def find_max_num_index(nums: List[int]) -> int:
        return nums.index(max(nums))

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # base case
        if len(nums) <= 1:
            return TreeNode(nums[0]) if len(nums) == 1 else None

        max_num_index = self.find_max_num_index(nums)
        root = TreeNode(nums[max_num_index])
        root.left = self.constructMaximumBinaryTree(nums[0:max_num_index])
        root.right = self.constructMaximumBinaryTree(nums[max_num_index + 1:])
        return root


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.construct_tree(nums, 0, len(nums) - 1)

    def construct_tree(self, nums, start, end):
        # 前序遍历递归
        mid = (start + end) // 2
        root = None if end - start < 0 else TreeNode(nums[mid])
        if root is None: return root

        root.left = self.construct_tree(nums, start, mid - 1)
        root.right = self.construct_tree(nums, mid + 1, end)
        return root


if __name__ == '__main__':
    pass

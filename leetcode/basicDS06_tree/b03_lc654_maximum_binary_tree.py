# https://leetcode-cn.com/problems/maximum-binary-tree/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.nums = list()

    def get_max_index(self, start_i: int, end_i: int) -> int:
        m_index, m_val = start_i, self.nums[start_i]
        for i in range(start_i, end_i + 1):
            if self.nums[i] > m_val:
                m_val = self.nums[i]
                m_index = i
        return m_index

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.dfs(0, len(self.nums) - 1)

    def dfs(self, start_i: int, end_i: int) -> TreeNode:
        # base case
        if start_i > end_i: return

        # 找到最大值及其索引
        m_index = self.get_max_index(start_i, end_i)
        root = TreeNode(self.nums[m_index])

        # 递归调用左右子树
        root.left = self.dfs(start_i, m_index - 1)
        root.right = self.dfs(m_index + 1, end_i)
        return root


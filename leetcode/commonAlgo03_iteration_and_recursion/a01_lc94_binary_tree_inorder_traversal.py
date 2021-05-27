# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        self.dfs(res, root)
        return res

    def dfs(self, nums: List[int], root: TreeNode):
        if not root: return

        self.dfs(nums, root.left)
        nums.append(root.val)
        self.dfs(nums, root.right)


if __name__ == '__main__':
    pass

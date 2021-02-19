# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # base case
        if len(preorder) <= 1:
            return TreeNode(preorder[0]) if len(preorder) == 1 else None

        root_val = preorder[0]
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1: inorder.index(root_val) + 1], inorder[0: inorder.index(root_val)])
        root.right = self.buildTree(preorder[inorder.index(root_val) + 1:], inorder[inorder.index(root_val) + 1:])
        return root


if __name__ == '__main__':
    pass

"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
leetcode 106 medium
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) <= 1:
            return TreeNode(inorder[0]) if len(inorder) == 1 else None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[0: inorder.index(root_val)], postorder[0: inorder.index(root_val)])
        root.right = self.buildTree(inorder[inorder.index(root_val) + 1:],
                                    postorder[inorder.index(root_val): len(postorder) - 1])
        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def search_bst(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return root

        if val == root.val:
            return root
        elif val > root.val:
            return self.search_bst(root.right, val)
        elif val < root.val:
            return self.search_bst(root.left, val)


if __name__ == '__main__':
    pass

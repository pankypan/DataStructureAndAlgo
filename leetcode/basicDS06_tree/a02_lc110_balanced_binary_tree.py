# https://leetcode-cn.com/problems/balanced-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True

        if abs(self.max_depth(root.left) - self.max_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    pass

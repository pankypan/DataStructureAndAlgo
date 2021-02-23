# https://leetcode-cn.com/problems/diameter-of-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 1

    def depth(self, node):
        if not node:
            return 0

        L = self.depth(node.left)
        R = self.depth(node.right)
        self.ans = max(self.ans, L + R + 1)  # DFS 过程中不断更新 ans
        return max(L, R) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        DFS
        :param root:
        :return:
        """
        self.depth(root)
        return self.ans - 1

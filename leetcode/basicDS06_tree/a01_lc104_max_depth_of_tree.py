# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # base case
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    @staticmethod
    def maxDepth2(root: TreeNode) -> int:
        max_depth = 0
        if root is None:
            return max_depth
        stack = list()
        stack.append((root, 1))  # 给每个结点标记层数

        while stack:
            node, depth = stack.pop()

            if not node.left and not node.right:
                max_depth = max(depth, max_depth)
                continue

            if node.right:
                stack.append((node.right, depth + 1))
                pass
            if node.left:
                stack.append((node.left, depth + 1))
                pass
        return max_depth


if __name__ == '__main__':
    pass

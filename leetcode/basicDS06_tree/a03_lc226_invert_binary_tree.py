# https://leetcode-cn.com/problems/invert-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # base case
        if root is None:
            return root

        # 前序遍历
        # root 节点需要交换它的左右子节点
        temp = root.left
        root.left = root.right
        root.right = temp

        # 递归翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        # base case
        if not root:
            return root

        # 后续遍历
        # 先翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 针对最后的根结点做操作
        root.left = right
        root.right = left
        return root


if __name__ == '__main__':
    pass

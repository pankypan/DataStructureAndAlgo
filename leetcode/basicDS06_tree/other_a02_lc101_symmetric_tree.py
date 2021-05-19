# https://leetcode-cn.com/problems/symmetric-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        return root1.val == root2.val and self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        DFS
        该问题可以转化为：两个树在什么情况下互为镜像？
        如果同时满足下面的条件，两个树互为镜像：
            它们的两个根结点具有相同的值
            每个树的右子树都与另一个树的左子树镜像对称
        :param root:
        :return:
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)


if __name__ == '__main__':
    pass

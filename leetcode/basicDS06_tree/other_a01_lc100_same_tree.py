# https://leetcode-cn.com/problems/same-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        DFS
        边界条件：
            验证相同的树，若当前节点都为空，返回true
            若仅有一个节点为空，说明不相同，返回false
        递归：
            对比当前节点的值，进入递归，p的左子树和q的左子树对比，p的右子树和q的右子树对比
        :param p:
        :param q:
        :return:
        """
        # 边界条件
        if p is None and q is None:  # p, q 均为 None
            return True
        if p is None or q is None:  # p, q 有一个为 None
            return False

        # 先比较根节点，再比较左右子树
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    pass

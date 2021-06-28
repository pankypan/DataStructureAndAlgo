from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = dict()
        self.res_lis = list()

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.traverse(root)
        return self.res_lis

    def traverse(self, root: TreeNode) -> str:
        """
        返回二叉树的序列化
        :param root:
        :return:
        """
        # 对于空节点，可以用一个特殊字符表示
        if not root: return '#'

        # 将左右子树序列化成字符串
        left_subtree_str = self.traverse(root.left)
        right_subtree_str = self.traverse(root.right)

        # 左右子树加上自己，就是以自己为根的二叉树序列化结果
        subtree_str = left_subtree_str + '_' + right_subtree_str + '_' + str(root.val)

        freq = self.memo.get(subtree_str, 0)
        # 多次重复也只会被加入结果集一次
        if freq == 1:
            self.res_lis.append(root)
        # 给子树对应的出现次数加一
        self.memo[subtree_str] = freq + 1
        return subtree_str


if __name__ == '__main__':
    pass

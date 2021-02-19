# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def levelOrder(root: TreeNode) -> List[List[int]]:
        """
        BFS
        :param root:
        :return:
        """
        res_lis = list()
        if not root:
            return res_lis

        queue = list()
        queue.append(root)

        while queue:
            level_length = len(queue)
            temp_lis = []
            for _ in range(level_length):
                node = queue.pop(0)
                temp_lis.append(node.val)

                if node.left:
                    queue.append(node.left)
                    pass
                if node.right:
                    queue.append(node.right)
                    pass
                pass
            res_lis.append(temp_lis)
        return res_lis

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        DFS
        :param root:
        :return:
        """
        res_lis = list()
        self.dfs(root, 0, res_lis)
        return res_lis

    def dfs(self, root: TreeNode, level: int, res_lis: list):
        if root is None:
            return

        if len(res_lis) == level:
            res_lis.append([root.val])
        else:
            res_lis[level].append(root.val)
            pass

        self.dfs(root.left, level + 1, res_lis)
        self.dfs(root.right, level + 1, res_lis)


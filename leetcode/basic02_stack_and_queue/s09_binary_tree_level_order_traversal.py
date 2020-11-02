"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
leetcode 102 medium
"""
from typing import List

from basic02_stack_and_queue.my_queues import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        核心：
            1.队列 + BFS
            2.记录分层
        :param root:
        :return:
        """
        res_lis = []
        if not root:
            return res_lis
        q = Queue()
        q.push(root)

        while not q.is_empty():
            level_size = q.size  # 记录每一层的结点的数量

            level_res = []
            for i in range(level_size):  # 处理(pop)完当前层的结点
                node = q.pop()
                level_res.append(node.val)

                if node.left is not None:
                    q.push(node.left)
                if node.right is not None:
                    q.push(node.right)
            res_lis.append(level_res)
        return res_lis


if __name__ == '__main__':
    pass

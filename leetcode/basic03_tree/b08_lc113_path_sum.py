# https://leetcode-cn.com/problems/path-sum-ii/
from typing import List
from copy import deepcopy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    record_lis = list()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res_lis = list()
        self.record_lis.clear()
        self.dfs(root, res_lis, sum)
        return res_lis

    def dfs(self, root, res_lis, target):
        if not root: return

        self.record_lis.append(root.val)
        self.dfs(root.left, res_lis, target)
        self.dfs(root.right, res_lis, target)

        # 在回溯位置进行判断
        if not root.left and not root.right:
            if sum(self.record_lis) == target:
                res_lis.append(deepcopy(self.record_lis))
        if self.record_lis:
            self.record_lis.pop()


if __name__ == '__main__':
    pass

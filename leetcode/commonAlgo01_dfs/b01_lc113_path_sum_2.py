# Definition for a binary tree node.
from copy import deepcopy
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret_lis = list()

        def dfs(node: TreeNode, track_path: list, dynamic_sum: int):
            # base case
            if not node: return

            # 做出选择，记录路径和动态和
            track_path.append(node.val)
            dynamic_sum -= node.val

            dfs(node.left, track_path, dynamic_sum)
            dfs(node.right, track_path, dynamic_sum)

            # 为根结点，且和满足条件
            if not node.left and not node.right:
                if dynamic_sum == 0:
                    ret_lis.append(deepcopy(track_path))
            # 回溯
            dynamic_sum += track_path.pop(-1)

        dfs(root, list(), targetSum)
        return ret_lis


if __name__ == '__main__':
    pass

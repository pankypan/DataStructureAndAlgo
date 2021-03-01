# https://leetcode-cn.com/problems/permutations/
from copy import deepcopy
from typing import List


class Solution:
    def __init__(self):
        self.ans, self.choices, self.track = list(), list(), list()

    def backtracking(self):
        # base case
        if len(self.track) == len(self.choices):
            self.ans.append(deepcopy(self.track))
            return

        for choice in self.choices:
            # 排除不合法的选择
            if choice in self.track: continue
            # 选择
            self.track.append(choice)
            # 进入下一层决策树
            self.backtracking()
            # 撤销选择
            self.track.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 初始化，挂载数据到对象空间
        self.ans, self.choices, self.track = list(), nums, list()

        # 回溯
        self.backtracking()
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    pass

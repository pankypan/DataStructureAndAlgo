# https://leetcode-cn.com/problems/combinations/
from copy import deepcopy
from typing import List


class Solution:
    def __init__(self):
        self.res, self.n, self.k = None, None, None

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        回溯算法，k 限制了树的高度，n 限制了树的宽度
        :param n:
        :param k:
        :return:
        """
        self.res, self.n, self.k = list(), n, k

        if k <= 0 or n <= 0: return self.res
        self.backtrack(1, list())
        return self.res

    def backtrack(self, start: int, track: list):
        # 到达树的底部
        if len(track) == self.k:
            self.res.append(deepcopy(track))
            return

        for i in range(start, self.n + 1):  # 注意 i 从 start 开始递增
            # 做选择
            track.append(i)
            # 下一层决策，递归
            self.backtrack(i + 1, track)
            # 撤销选择
            track.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    pass

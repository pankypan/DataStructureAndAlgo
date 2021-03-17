from copy import deepcopy
from typing import List


class Solution:
    def __init__(self):
        self.candidates, self.length, self.target, self.res = list(), 0, 0, list()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯算法
        使用减法，达到减支的效果(target不断变小)
        :param candidates:
        :param target:
        :return:
        """
        self.candidates, self.res, self.length = candidates, list(), len(candidates)
        self.backtracking(0, list(), target)
        return self.res

    def backtracking(self, begin: int, track_path: list, target):
        """
        我们在搜索的时候就需要 按某种顺序搜索。具体的做法是：每一次搜索的时候设置 下一轮搜索的起点 begin，实现路径去重
        :param begin:
        :param track_path:
        :param target:
        :return:
        """
        # base case
        if target < 0: return
        if target == 0:
            self.res.append(deepcopy(track_path))
            return

        for index in range(begin, self.length):
            # 减支：过滤不合适的数
            if self.candidates[index] > target: continue

            track_path.append(self.candidates[index])
            target -= self.candidates[index]

            self.backtracking(index, track_path, target)

            pop_num = track_path.pop()
            target += pop_num


if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum([2, 3, 6, 7], 7)
    print(res)
    pass

# https://leetcode-cn.com/problems/subsets/
from copy import deepcopy
from typing import List


class Solution:
    def __init__(self):
        self.res, self.nums = None, None

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        递归(数学归纳法)
        第一个解法是利用数学归纳的思想：假设我现在知道了规模更小的子问题的结果，如何推导出当前问题的结果呢？
        具体来说就是，现在让你求 [1,2,3] 的子集，如果你知道了 [1,2] 的子集，是否可以推导出 [1,2,3] 的子集呢？先把 [1,2] 的子集写出来瞅瞅：
        [ [],[1],[2],[1,2] ]
        你会发现这样一个规律：
        subset([1,2,3]) - subset([1,2])
        = [3],[1,3],[2,3],[1,2,3]
        而这个结果，就是把 sebset([1,2]) 的结果中每个集合再添加上 3。
        换句话说，如果 A = subset([1,2]) ，那么：
        subset([1,2,3])
        = A + [A[i].add(3) for i = 1..len(A)]
        :param nums:
        :return:
        """
        # base case
        if len(nums) == 0: return [[]]

        sub_res = self.subsets1(nums[:-1])
        return sub_res + [[nums[-1]] + subset for subset in sub_res]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        回溯算法
            重点：动态的start实现了对全排列树的减支，成为子集树
        :param nums:
        :return:
        """
        self.res, self.nums = list(), nums
        self.backtrack(0, list())
        return self.res

    def backtrack(self, start: int, track: list):
        self.res.append(deepcopy(track))

        for i in range(start, len(self.nums)):  # 动态的 start 实现了对全排列树的减支
            # 做选择
            track.append(self.nums[i])
            # 进入下一层决策
            self.backtrack(i + 1, track)
            # 撤销选择
            track.pop()


if __name__ == '__main__':
    s = Solution()
    # print(s.subsets1([1, 2]))
    # print(s.subsets1([1, 2, 3]))

    print(s.subsets([1, 2, 3]))

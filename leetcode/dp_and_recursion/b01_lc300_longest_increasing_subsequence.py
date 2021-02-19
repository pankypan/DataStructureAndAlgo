# https://leetcode-cn.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i] ：表示以nums[i]结尾的最长上升子序列的长度
        :param nums:
        :return:
        """
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    pass

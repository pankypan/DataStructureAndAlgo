# https://leetcode-cn.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] : 偷盗 至 第 i个房子时，所获取的最大利益
        :param nums:
        :return:
        """
        if len(nums) == 0: return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp)
        return int(max(dp))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
    pass

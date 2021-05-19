# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP：
        考虑到「不能同时参与多笔交易」，因此每天交易结束后只可能存在手里有一支股票或者没有股票的状态。
        定义状态dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，commonAlgo05_dp_and_recursion[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）。

        考虑 commonAlgo05_dp_and_recursion[i][0] 的转移方程，如果这一天交易完后手里没有股票，那么可能的转移状态为前一天已经没有股票，即 commonAlgo05_dp_and_recursion[i−1][0]，
        或者前一天结束的时候手里持有一支股票，即 commonAlgo05_dp_and_recursion[i−1][1]，这时候我们要将其卖出，并获得 prices[i] 的收益。
        因此为了收益最大化，我们列出如下的转移方程：
                    commonAlgo05_dp_and_recursion[i][0] = max(commonAlgo05_dp_and_recursion[i - 1][0], commonAlgo05_dp_and_recursion[i - 1][1] + prices[i])
        再来考虑 commonAlgo05_dp_and_recursion[i][1]，按照同样的方式考虑转移状态，那么可能的转移状态为前一天已经持有一支股票，即 commonAlgo05_dp_and_recursion[i−1][1]，
        或者前一天结束时还没有股票，即 commonAlgo05_dp_and_recursion[i−1][0]，这时候我们要将其买入，并减少 prices[i] 的收益。
        可以列出如下的转移方程：
                    commonAlgo05_dp_and_recursion[i][1] = max(commonAlgo05_dp_and_recursion[i - 1][0] - prices[i], commonAlgo05_dp_and_recursion[i - 1][1])
        :param prices:
        :return:
        """
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        return dp[len(prices) - 1][0]


if __name__ == '__main__':
    pass

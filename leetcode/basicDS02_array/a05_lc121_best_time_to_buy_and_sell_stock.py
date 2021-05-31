# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        一次遍历
            假设在第 i 天，如果我们要在今天卖股票，那么我们能赚多少钱呢？

            显然，如果我们真的在买卖股票，我们肯定会想：如果我是在历史最低点买的股票就好了！
            太好了，在题目中，我们只要用一个变量记录一个历史最低价格 minprice，我们就可以假设自己的股票是在那天买的。
            那么我们在第 i 天卖出股票能得到的利润就是 prices[i] - minprice。
        :param prices:
        :return:
        """
        min_price, max_profit = prices[0], 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price if price - min_price > 0 else 0
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
    pass

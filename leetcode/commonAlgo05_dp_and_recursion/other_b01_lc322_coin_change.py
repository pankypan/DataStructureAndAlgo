"""
https://leetcode-cn.com/problems/coin-change/
LeetCode 322
"""
from typing import List


class Solution:
    def coin_change_recursion(self, coins: List[int], amount: int) -> int:
        # base case
        if amount < 0: return -1
        if amount == 0: return 0

        # 求最小值，所以初始化未正无穷
        res = float('INF')
        for coin in coins:
            sub_problem = self.coin_change_recursion(coins, amount - coin)
            # 子问题无解，跳过
            if sub_problem == -1: continue
            res = min(res, 1 + sub_problem)
        return res if res != float('INF') else -1

    def coin_change_memory_recur(self, coins: List[int], amount: int) -> int:
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]

            # base case
            if n < 0: return -1
            if n == 0: return 0

            # 求最小值，所以初始化未正无穷
            res = float('INF')
            for coin in coins:
                sub_problem = dp(n - coin)
                # 子问题无解，跳过
                if sub_problem == -1: continue
                res = min(res, 1 + sub_problem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]
        return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        动态规划
        :param coins: 可选硬币值
        :param amount: 目标金额
        :return: -1 表示不能凑出， x 表示最少需要x枚硬币凑出目标金额
        """
        # dp数组大小为 amount + 1, 初始值也为 amount + 1
        # 初始化为 amount + 1 就相当于初始化为正无穷，便于后续取最小值。
        dp_arr = [amount + 1] * (amount + 1)

        # base case
        dp_arr[0] = 0

        # 外层 for 循环，遍历所有状态的所有取值, i 表示金额
        for i in range(amount + 1):
            # 内层 for 循环，求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin < 0: continue
                dp_arr[i] = min(dp_arr[i], dp_arr[i - coin] + 1)
                pass
            pass
        return dp_arr[amount] if dp_arr[amount] != amount + 1 else -1


if __name__ == "__main__":
    pass


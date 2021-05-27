"""
https://leetcode-cn.com/problems/fibonacci-number/
LeetCode 509
"""


class Solution:
    def fib_recursion(self, n: int) -> int:
        """暴力递归法"""
        # base case
        if n <= 0:
            return 0
        if n == 1:
            return 1

        return self.fib_recursion(n - 1) + self.fib_recursion(n - 2)

    def helper(self, memory: list, n: int):
        # base case
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # 已经计算过
        if memory[n] != 0:
            return memory[n]
        # 未计算过,计算并记录
        memory[n] = self.helper(memory, n - 1) + self.helper(memory, n - 2)
        return memory[n]

    def fib_memo_recur(self, n: int) -> int:
        """带备忘录的递归法，记忆优化"""
        if n < 1:
            return 0
        # 备忘录全部初始化未 0
        memory = [0] * (n + 1)
        # 进行带备忘录的递归
        return self.helper(memory, n)

    def fib_dp(self, n: int) -> int:
        """动态规划"""
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # 初始化 commonAlgo09_dp 数组
        dp = [0] * (n + 1)

        # base case
        dp[0], dp[1] = 0, 1

        # 自底向上迭代
        for i in range(2, n + 1):
            # 状态转移方程
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def fib_dp_state_compress(n: int) -> int:
    """动态规划，使用状态压缩"""
    # base case
    if n <= 0:
        return 0
    if n == 1:
        return 1

    pre, cur = 0, 1
    for i in range(2, n + 1):
        sum_int = pre + cur
        pre = cur
        cur = sum_int
    return sum_int


def print_result_and_cal_time(f, *args):
    import time
    start = time.time()
    result = f(*args)
    print("result: ", result, "used time:", time.time() - start)


if __name__ == "__main__":
    print_result_and_cal_time(fib_dp_state_compress, 30)

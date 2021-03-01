# https://leetcode-cn.com/problems/climbing-stairs/


class Solution:
    cache = {}  # 缓存，解决递归的重复计算

    def climbStairs(self, n: int) -> int:
        """
        递归公式: f(n) = f(n-1) + f(n-2)
        :param n:
        :return:
        """
        if self.cache.get(n):
            return self.cache.get(n)
        if n <= 2:
            return n
        ret = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = ret
        return ret

    def climbStairsDP(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))
    print(s.climbStairsDP(5))
    print(s.climbStairsDP(2))

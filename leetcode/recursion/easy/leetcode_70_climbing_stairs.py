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
        print(self.cache)
        return ret


if __name__ == '__main__':
    s = Solution()
    # print(s.climbStairs(3))
    print(s.climbStairs(5))

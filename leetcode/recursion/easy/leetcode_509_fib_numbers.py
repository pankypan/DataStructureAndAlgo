class Solution:
    cache = {}  # 缓存

    def fib(self, N: int) -> int:
        if self.cache.get(N):  # 获取缓存
            return self.cache.get(N)
        if N == 0:
            return 0
        if N == 1:
            return 1
        ret = self.fib(N - 1) + self.fib(N - 2)
        self.cache[N] = ret
        return ret

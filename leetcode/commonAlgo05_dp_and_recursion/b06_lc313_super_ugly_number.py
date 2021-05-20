# commonAlgo05_dp_and_recursion https://leetcode-cn.com/problems/super-ugly-number/
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        DP
        K个指针指向dp中的元素，最小的丑数只可能出现在如dp[l2]的2倍、dp[l7]的7倍、dp[l13]的13倍和dp[l19]的19倍四者中间。通过移动K个指针，
        就能保证生成的丑数是有序的。通过求到最小值来保证丑数数组有序排列。
        :param n:
        :param primes:
        :return:
        """
        dp = [0] * n
        pointers = [0] * len(primes)

        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(prime * dp[pointer] for prime, pointer in zip(primes, pointers))

            for j in range(len(primes)):
                if dp[i] == primes[j] * dp[pointers[j]]:
                    pointers[j] += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.nthSuperUglyNumber(12, [2, 7, 13, 19])
    pass

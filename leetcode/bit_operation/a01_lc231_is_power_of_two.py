# https://leetcode-cn.com/problems/power-of-two/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """对于N为2的幂的数，都有 N&(N-1)=0"""
        if n == 0: return False
        return n & (n - 1) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(8))
    print(s.isPowerOfTwo(6))
    pass

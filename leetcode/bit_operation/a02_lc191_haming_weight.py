# https://leetcode-cn.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        以构造一个掩码来进行, 要让这个掩码每次向左移动一位，然后与目标值求“&”，就可以判断目标值的当前位是不是1。
        :param n:
        :return:
        """
        mask = 1
        result = 0

        for _ in range(32):
            if n & mask != 0:
                result += 1
            mask = mask << 1
        return result

    def hammingWeight2(self, n: int) -> int:
        """位运算小技巧: 对于任意一个数，将 n 和 n-1 进行 & 运算，我们都可以把 n 中最低位的 1 变成 0"""
        count = 0

        while n > 0:
            n &= n - 1
            count += 1
        return count


if __name__ == '__main__':
    pass

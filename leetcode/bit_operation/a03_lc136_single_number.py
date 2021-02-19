# https://leetcode-cn.com/problems/single-number/
from typing import List
"""
异或操作的性质：
    1.任意一个数和0异或仍然为自己：  x ^ 0 = x
    2.任意一个数和自己异或是0：     x ^ x = 0
    3.异或操作满足交换律和结合律：   a ^ b ^ a = (a ^ a) ^ b = b
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 1, 2, 1, 2]))
    pass

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """两个相同的数，使用异或可以相消除"""
        n = len(nums)
        a, b = 1, 1

        for num in nums:
            a ^= num
        for i in range(n + 1):
            b ^= i
        return a ^ b


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
    pass

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """把原数组去重、再乘以3得到的值，刚好就是要找的元素的2倍"""
        return int((sum(set(nums)) * 3 - sum(nums)) / 2)


if __name__ == '__main__':
    pass

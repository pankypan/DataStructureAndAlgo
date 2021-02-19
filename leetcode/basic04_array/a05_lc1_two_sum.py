# https://leetcode-cn.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dic = dict()

        for index, num in enumerate(nums):
            res = target - num
            if res in map_dic:
                return [map_dic[res], index]
            map_dic[num] = index
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 2, 4], 8))
    print(s.twoSum([3, 3], 6))
    pass

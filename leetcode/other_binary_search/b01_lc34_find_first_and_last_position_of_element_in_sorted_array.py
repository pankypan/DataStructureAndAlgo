# binary_search https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def __init__(self):
        self.nums, self.target = list(), int()

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]
        self.nums, self.target = nums, target

        one_target_index = self.binary_search(0, len(nums) - 1)
        if one_target_index == -1: return ret

        # move cursor
        l_cur, r_cur = one_target_index, one_target_index
        while l_cur >= 0 and self.nums[l_cur] == self.target:
            l_cur -= 1
        while r_cur <= len(nums) - 1 and self.nums[r_cur] == self.target:
            r_cur += 1
        return [l_cur + 1, r_cur - 1]

    def binary_search(self, left, right):
        # base case
        if left > right: return -1
        if right - left == 1:
            if self.nums[left] == self.target or self.nums[right] == self.target:
                return left if self.nums[left] == self.target else right
            else:
                return -1
        if right == left:
            if self.target != self.nums[left]: return -1

        middle = (left + right) // 2
        if self.target > self.nums[middle]:
            return self.binary_search(middle, right)
        elif self.target < self.nums[middle]:
            return self.binary_search(left, middle)
        else:
            return middle


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(s.searchRange([], 0))
    print(s.searchRange([1], 0))
    print(s.searchRange([1, 4], 4))
    pass

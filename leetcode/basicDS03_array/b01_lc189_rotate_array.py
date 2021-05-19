# https://leetcode-cn.com/problems/rotate-array/
from typing import List


class Solution:
    def reverse(self,nums: List[int], head: int, tail: int):
        while head < tail:
            nums[head], nums[tail] = nums[tail], nums[head]
            head += 1
            tail -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        我们只需要将所有元素反转，然后反转前 k 个元素，
        再反转后面 l-k 个元素，就能得到想要的结果。
        """
        length = len(nums)
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k % length - 1)
        self.reverse(nums, k % length, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    n_array = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(n_array, 3)
    print(n_array)
    pass

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        双指针：保留两个指针 ii 和 jj，其中 ii 是慢指针，jj 是快指针。
        当 nums[j] 与给定的值相等时，递增 j 以跳过该元素。只要 nums[j] !=val，我们就复制 nums[j] 到 nums[i] 并同时递增两个索引。
        重复这一过程，直到 j 到达数组的末尾，该数组的新长度为 i。
        :param nums:
        :param val:
        :return:
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    s = Solution()
    n_arr = [0, 1, 2, 2, 3, 0, 4, 2]
    print(s.removeElement(n_arr, 2))
    print(n_arr)
    pass

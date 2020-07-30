class Solution:
    def move_zeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        non_zeros_length = length
        for i in range(length - 1, -1, -1):
            if nums[i] == 0:
                j = i
                while j < non_zeros_length - 1:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
                non_zeros_length -= 1

    def moveZeroes(self, nums) -> None:
        """
        双指针
        :param nums:
        :return:
        """
        length = len(nums)
        cur_p = 0  # 遍历指针，用于逐个遍历数组元素
        record_p = 0  # 辅助记录指针，用于记录非0数的指针

        while cur_p < length:
            if nums[cur_p] != 0:  # 当前元素!=0，就把其交换到左边，等于0的交换到右边，并移动辅助记录指针
                nums[record_p], nums[cur_p] = nums[cur_p], nums[record_p]
                record_p += 1
            cur_p += 1  # 移动遍历指针


if __name__ == '__main__':
    s = Solution()
    t_lis = [0, 1, 0, 3, 12]
    s.moveZeroes(t_lis)
    print(t_lis)


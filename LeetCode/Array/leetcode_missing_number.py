class Solution:
    @staticmethod
    def missing_number(nums: list) -> int:
        """
        单循环方法
        :param nums:
        :return:
        """
        miss_number = None
        for i, v in enumerate(nums):
            if i != v:
                miss_number = i
                break
        if miss_number is None:
            miss_number = len(nums)
        return miss_number

    @staticmethod
    def missing_number_2(nums: list) -> int:
        """
        二分法
        :param nums:
        :return:
        """
        length = len(nums)
        if nums[-1] == length - 1:
            return length

        i, j = 0, length - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.missing_number([0, 1, 3]))
    print(s.missing_number([0, 1, 2, 3, 4, 5, 6, 7, 9]))
    print(s.missing_number([0]))
    print(s.missing_number([0, 1]))
    print(s.missing_number_2([0, 1, 3, 4, 5]))
    print(s.missing_number_2([0, 1, 3]))

# find all numbers disappeared in an array


class Solution:
    def find_disappeared_numbers(self, nums: list) -> list:
        print(self)
        for i in range(len(nums)):
            while True:
                if nums[i] - 1 == i or nums[nums[i] - 1] == nums[i]:
                    break
                else:
                    j = nums[i] - 1
                    nums[i], nums[j] = nums[j], nums[i]
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res

    @staticmethod
    def get_abs(x):
        return x if x >= 0 else x * -1

    def findDisappearedNumbers(self, nums: list) -> list:
        """
        Algo
            遍历输入数组的每个元素一次。
            我们将把 |nums[i]|-1 索引位置的元素标记为负数。即 nums[∣nums[i]∣−1]×−1 。
            然后遍历数组，若当前数组元素 nums[i] 为负数，说明我们在数组中存在数字 i+1。
        :param nums:
        :return:
        """
        for i in range(len(nums)):
            if nums[self.get_abs(nums[i]) - 1] > 0:
                nums[self.get_abs(nums[i]) - 1] = nums[self.get_abs(nums[i]) - 1] * -1
        print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

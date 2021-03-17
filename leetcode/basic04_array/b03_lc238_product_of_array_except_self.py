from typing import List


class Solution:
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        """
        左右乘积列表
        :param nums:
        :return:
        """
        nums_length = len(nums)
        l_product, r_product = [1] * nums_length, [1] * nums_length

        for i in range(1, nums_length):
            l_product[i] = l_product[i - 1] * nums[i - 1]

        for i in range(nums_length - 2, -1, -1):
            r_product[i] = nums[i + 1] * r_product[i + 1]
        return list(map(lambda x, y: x * y, l_product, r_product))

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        降低空间复杂度
            用一个 R 来跟踪右边元素的乘积
        :param nums:
        :return:
        """
        nums_length = len(nums)
        ans = [1] * nums_length

        for i in range(1, nums_length):
            ans[i] = ans[i - 1] * nums[i - 1]

        R = nums[-1]
        for i in range(nums_length - 2, -1, -1):
            ans[i] = ans[i] * R
            R *= nums[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([4, 5, 1, 8, 2]))
    pass

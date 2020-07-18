class Solution:
    def majorityElement(self, nums: list) -> int:
        """
        哈希表法
        :param nums:
        :return:
        """
        count_dic = {}
        for i in nums:
            if i not in count_dic:
                count_dic[i] = 0
            else:
                count_dic[i] += 1
        return max(count_dic, key=lambda key: count_dic[key])

    def majority_element(self, nums: list):
        """
        Boyer-Moore 算法的本质和方法四中的分治十分类似。我们首先给出 Boyer-Moore 算法的详细步骤：
        我们维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；

        我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，
        随后我们判断 x：
            如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
            如果 x 与 candidate 不等，那么计数器 count 的值减少 1。

        在遍历完成后，candidate 即为整个数组的众数。
        :param nums:
        :return:
        """
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            if x == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(s.majority_element([3, 2, 3]))
    print(s.majority_element([2, 2, 1, 1, 1, 2, 2]))

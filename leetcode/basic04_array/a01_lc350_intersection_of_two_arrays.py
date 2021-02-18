from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_dic = dict()
        res = list()
        for num in nums1:
            if num not in map_dic:
                map_dic[num] = 1
            else:
                map_dic[num] += 1

        for num in nums2:
            if map_dic.get(num, 0) > 0:
                res.append(num)
                map_dic[num] -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(s.intersect([1, 2, 2, 1], [2, 2]))
    pass

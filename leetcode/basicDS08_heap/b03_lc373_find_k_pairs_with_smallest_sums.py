# basicDS08_heap https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        length1, length2 = len(nums1), len(nums2)
        priority_queue = list()
        ret_lis = list()

        def push_item(i, j):
            if i < length1 and j < length2:
                heapq.heappush(priority_queue, [nums1[i] + nums2[j], i, j])

        # 从矩阵左上角开始
        i, j = 0, 0
        heapq.heappush(priority_queue, [nums1[i] + nums2[j], i, j])
        while priority_queue and len(ret_lis) < k:
            _, i, j = heapq.heappop(priority_queue)
            ret_lis.append([nums1[i], nums2[j]])

            # 每当将一对选择为输出结果时，该行中的下一对就会添加到当前选项的优先队列中
            push_item(i, j + 1)
            # 如果所选对是该行中的第一对，则将下一行中的第一对添加到队列中
            if j == 0:
                push_item(i + 1, j)
        return ret_lis


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
    print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))

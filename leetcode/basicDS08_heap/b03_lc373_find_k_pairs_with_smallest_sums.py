# basicDS08_heap https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/
import heapq
from typing import List


class CompareObj(object):
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __lt__(self, other):
        return sum([self.n1, self.n2]) < sum([other.n1, other.n2])

    def __gt__(self, other):
        return sum([self.n1, self.n2]) > sum([other.n1, other.n2])

    def __eq__(self, other):
        return (self.n1 + self.n2) == (other.n1 + other.n2)


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap_lis = list()

        count = 0
        for n1 in nums1:
            for n2 in nums2:
                item = CompareObj(n1, n2)
                if count < k:
                    heapq.heappush(heap_lis, item)
                else:
                    if item < heap_lis[0] or item == heap_lis[0]:
                        heapq.heapreplace(heap_lis, item)
                count += 1
        return [[item.n1, item.n2] for item in heap_lis]


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
    print(s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
    pass

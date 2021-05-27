# basicDS05_heap https://leetcode-cn.com/problems/top-k-frequent-elements/
import heapq
from typing import List


class CompareObj(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __lt__(self, other):
        return self.v < other.v

    def __gt__(self, other):
        return self.v > other.v


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record_hash_table = dict()
        res_heap = list()

        for number in nums:
            if number not in record_hash_table:
                record_hash_table[number] = 1
            else:
                record_hash_table[number] += 1

        count = 0
        for key, val in record_hash_table.items():
            item_obj = CompareObj(key, val)
            if count < k:
                heapq.heappush(res_heap, item_obj)
            else:
                if res_heap[0] < item_obj:
                    heapq.heapreplace(res_heap, item_obj)
            count += 1
        return [item.k for item in res_heap]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))
    pass

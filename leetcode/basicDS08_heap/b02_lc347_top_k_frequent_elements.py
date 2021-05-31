# basicDS05_heap https://leetcode-cn.com/problems/top-k-frequent-elements/
import heapq
from typing import List


class Solution:
    @staticmethod
    def get_num_statics(nums) -> dict:
        hash_table = dict()
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        return hash_table

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = self.get_num_statics(nums)

        priority_queue = list()
        count = 0
        for key, val in hash_table.items():
            if count < k:
                heapq.heappush(priority_queue, [val, key])
            else:
                if val > priority_queue[0][0]:
                    heapq.heappop(priority_queue)
                    heapq.heappush(priority_queue, [val, key])
            count += 1
        return [item_lis[1] for item_lis in priority_queue]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))

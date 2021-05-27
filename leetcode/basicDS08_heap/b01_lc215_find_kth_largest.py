# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        """
        Heap
            使用容量为 k 的小顶堆
            元素个数小于 k 的时候，放进去就是了
            元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换
        """
        priority_queue = list()

        for i in range(k):
            heapq.heappush(priority_queue, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > priority_queue[0]:
                heapq.heapreplace(priority_queue, nums[i])
        return priority_queue[0]


if __name__ == '__main__':
    pass

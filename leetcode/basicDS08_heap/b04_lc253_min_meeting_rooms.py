import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 按会议开始时间进行排序
        intervals.sort(key=lambda item: item[0])

        priority_queue = list()
        heapq.heappush(priority_queue, intervals[0][1])

        for i in range(1, len(intervals)):
            meeting = intervals[i]
            # meeting 完全大于堆顶 则 堆顶空闲
            if meeting[0] >= priority_queue[0]:  # 房间空闲: meeting 的开始时间 大于堆顶的 结束时间
                heapq.heappop(priority_queue)
                heapq.heappush(priority_queue, meeting[1])
            else:  # 房间不空闲
                heapq.heappush(priority_queue, meeting[1])

        return len(priority_queue)


if __name__ == '__main__':
    s = Solution()
    print(s.minMeetingRooms([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]))
    print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(s.minMeetingRooms([[7, 10], [2, 4]]))

# commonAlgo08_greedy https://leetcode-cn.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        贪心  最远可达位置

        我们依次遍历数组中的每一个位置，并实时维护 最远可以到达的位置。对于当前遍历到的位置 x，如果它在 最远可以到达的位置 的范围内，
        那么我们就可以从起点通过若干次跳跃到达该位置，因此我们可以用 x + nums[x] 更新 最远可以到达的位置。
        :param nums:
        :return:
        """
        last_index = len(nums) - 1
        furthest_index = 0

        for cur_index in range(0, last_index + 1):
            if cur_index > furthest_index: return False

            furthest_index = max(cur_index + nums[cur_index], furthest_index)
            if furthest_index >= last_index:
                return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))

# https://leetcode-cn.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        暴力法:
            对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。
        """
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        ans = 0

        for index, num in enumerate(height):
            left_max = max(height[0: index + 1])
            right_max = max(height[index:])
            ans += min(left_max, right_max) - num if min(left_max, right_max) > num else 0
        return ans

    def trap2(self, height: List[int]) -> int:
        """动态规划法"""
        ans = 0
        length = len(height)
        if length == 0: return ans

        left_max_arr = [height[0]] * length
        right_max_arr = [height[length - 1]] * length
        for i in range(1, length):
            left_max_arr[i] = max(height[i], left_max_arr[i - 1])
        for i in range(length - 2, -1, -1):
            right_max_arr[i] = max(height[i], right_max_arr[i + 1])
        for index, num in enumerate(height):
            border = min(left_max_arr[index], right_max_arr[index])
            ans += border - num if border > num else 0
        return ans

    def trap3(self, height: List[int]) -> int:
        """单调递减栈"""
        ans = 0
        stack = list()

        for index, num in enumerate(height):
            while len(stack) > 0 and num > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break

                distance = index - stack[-1] - 1
                bounded_height = min(num, height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(index)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap2([4, 2, 0, 3, 2, 5]))
    print(s.trap3([4, 2, 0, 3, 2, 5]))
    pass

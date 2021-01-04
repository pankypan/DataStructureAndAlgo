"""
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
leetcode 84 hard
"""
from basic02_stack_and_queue.my_stacks import Stack
from typing import List


class Solution:
    @staticmethod
    def get_width(index, heights: List[int]) -> int:
        left_border = index - 1
        right_border = index + 1

        # broaden left
        while left_border >= 0 and heights[index] <= heights[left_border]:
            left_border -= 1
        # broaden right
        while right_border < len(heights) and heights[index] <= heights[right_border]:
            right_border += 1
        return right_border - left_border - 1

    def largestRectangleArea_1(self, heights: List[int]) -> int:
        """暴力法：固定高"""
        lis_len = len(heights)
        max_area = 0

        for i in range(lis_len):
            width = self.get_width(i, heights)
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        单调栈(单增): 保持栈顶为当前栈最大元素
        我们在缓存数据的时候，是从左向右缓存的，
        我们计算出一个结果的顺序是从右向左的，并且计算完成以后我们就不再需要了，
        符合后进先出的特点。因此，我们需要的这个作为缓存的数据结构就是栈。
        """
        lis_len = len(heights)
        max_area = 0

        stack = Stack()

        for i in range(lis_len):
            while not stack.is_empty() and heights[i] < stack.peek()[1]:
                index, cur_height = stack.pop()

                # 处理相等的特殊情况
                while not stack.is_empty() and heights[i] == stack.peek():
                    stack.pop()

                if stack.is_empty():
                    cur_width = i
                else:
                    cur_width = i - stack.peek()[0] - 1

                max_area = max(max_area, cur_height * cur_width)
            stack.push([i, heights[i]])

        while not stack.is_empty():
            index, cur_height = stack.pop()

            while not stack.is_empty() and cur_height == stack.peek()[1]:
                stack.pop()

            if stack.is_empty():
                cur_width = lis_len
            else:
                cur_width = lis_len - stack.peek()[0] - 1

            max_area = max(max_area, cur_height * cur_width)
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 2]))

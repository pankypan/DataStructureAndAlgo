# https://leetcode-cn.com/problems/rotate-image/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        # 1.以对角线（左上<—>右下）为轴进行翻转
        for i in range(length):
            cur = i
            while cur < length:
                matrix[i][cur], matrix[cur][i] = matrix[cur][i], matrix[i][cur]
                cur += 1

        # 2.对每行左右翻转
        for row in range(length):
            left, right = 0, length - 1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left, right = left + 1, right - 1


if __name__ == '__main__':
    lis = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    s.rotate(lis)
    print(lis)

    lis = [[1]]
    s.rotate(lis)
    print(lis)
    pass

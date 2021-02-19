# https://leetcode-cn.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        dp[i][j] : 表示包含第i行j列元素的最小路径和
        :param triangle:
        :return:
        """
        length = len(triangle)
        dp = [[float('INF') for _ in range(length)] for _ in range(length)]
        dp[0][0] = triangle[0][0]

        for i in range(1, length):
            for j in range(i + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        print(dp)
        return int(min(dp[-1]))


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    pass

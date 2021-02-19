# https://leetcode-cn.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp[i][j] : 表示包含第i行j列元素的最小路径和
        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        dp = [[float('INF') for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return int(dp[-1][-1])


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
    pass

# https://leetcode-cn.com/problems/n-queens/
from typing import List


class Solution:
    def __init__(self):
        self.board, self.ans = list(), list()

    def init_board(self, n):
        self.board = [['.' for _ in range(n)] for _ in range(n)]

    def is_valid(self, row: int, col: int):
        """
        是否可以在 board[row][col] 放置皇后？
        :param row:
        :param col:
        :return:
        """
        n = len(self.board)

        # 检查列是否有皇后互相冲突
        for i in range(n):
            if self.board[i][col] == 'Q': return False

        # 检查右上方是否有皇后互相冲突
        i, j = row -1, col + 1
        while i >= 0 and j < n:
            if self.board[i][j] == 'Q': return False
            i, j = i - 1, j + 1

        # 检查左上方是否有皇后互相冲突
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q': return False
            i, j = i - 1, j - 1

        return True

    def backtracking(self, row: int):
        """
        路径：board 中小于 row 的那些行都已经成功放置了皇后
        选择列表：第 row 行的所有列都是放置皇后的选择
        结束条件：row 超过 board 的最后一行
        :param row:
        :return:
        """
        # 结束条件
        if row == len(self.board):
            self.ans.append([''.join(row) for row in self.board])
            return

        n_col = len(self.board[row])
        for col in range(n_col):
            # 排除不合法选择
            if not self.is_valid(row, col): continue
            # 做选择
            self.board[row][col] = 'Q'
            # 进入下一层决策
            self.backtracking(row + 1)
            # 撤销选择
            self.board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = list()
        # '.' 表示空，'Q' 表示皇后，初始化空棋盘
        self.init_board(n)

        # 回溯
        self.backtracking(0)
        return self.ans


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
    pass

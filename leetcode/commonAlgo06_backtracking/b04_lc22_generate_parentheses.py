# https://leetcode-cn.com/problems/generate-parentheses/
from copy import deepcopy
from typing import List


class Solution:
    def __init__(self):
        self.ans, self.n = list(), 0

    def valid(self, parenthesis_lis: list):
        bal = 0
        for c in parenthesis_lis:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0: return False
        return bal == 0

    def generateParenthesis(self, n: int) -> List[str]:
        """
        方法1：暴力回溯
        :param n:
        :return:
        """
        self.ans, self.n = list(), n
        self.backtrack([])
        return self.ans

    def backtrack(self, p_lis: list):
        if len(p_lis) == 2 * self.n:
            if self.valid(p_lis):
                self.ans.append("".join(p_lis))
            return

        for par in ('(', ')'):  # 两种选择 '(', ')' 先后顺序很重要
            p_lis.append(par)
            self.backtrack(p_lis)
            p_lis.pop()

    def generateParenthesis2(self, n: int) -> List[str]:
        """
        方法2：回溯改进
            方法一还有改进的余地：我们可以只在序列仍然保持有效时才添加 '(' or ')'，而不是像 方法一 那样每次添加。我们可以通过跟踪到目前为止
            放置的左括号和右括号的数目来做到这一点，如果左括号数量不大于 n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以
            放一个右括号。
        :param n:
        :return:
        """
        self.ans, self.n = list(), n
        self.backtrack2([], 0, 0)
        return self.ans

    def backtrack2(self, p_lis: list, left: int, right: int):
        if len(p_lis) == 2 * self.n:
            self.ans.append("".join(p_lis))
            return

        # 两种选择 '(', ')' 先后顺序很重要
        if left < self.n:
            p_lis.append('(')
            self.backtrack2(p_lis, left + 1, right)
            p_lis.pop()
        if right < left:
            p_lis.append(')')
            self.backtrack2(p_lis, left, right + 1)
            p_lis.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis2(3))
    pass

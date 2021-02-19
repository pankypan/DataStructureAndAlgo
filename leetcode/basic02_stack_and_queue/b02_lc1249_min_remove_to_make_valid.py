# https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:
        mapping = {'(': ')'}
        stack = []

        to_remove = []
        for i, char in enumerate(s):
            if char in mapping:
                stack.append(i)
            if char == ')':
                if not stack:
                    to_remove.append(i)
                else:
                    stack.pop()
        to_remove += stack
        return ''.join([v for i, v in enumerate(s) if i not in to_remove])


if __name__ == '__main__':
    s = Solution()
    print(s.min_remove_to_make_valid("lee(t(c)o)de)"))
    print(s.min_remove_to_make_valid("a)b(c)d"))
    print(s.min_remove_to_make_valid("))(("))
    print(s.min_remove_to_make_valid("(a(b(c)d)"))

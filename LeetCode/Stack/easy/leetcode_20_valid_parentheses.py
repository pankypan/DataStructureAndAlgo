class Solution:
    def is_valid(self, s: str) -> bool:
        """
        算法
        初始化栈 S。
            1. 一次处理表达式的每个括号。
            2. 如果遇到开括号，我们只需将其推到栈上即可。这意味着我们将稍后处理它，让我们简单地转到前面的 子表达式。
            3. 如果我们遇到一个闭括号，那么我们检查栈顶的元素。如果栈顶的元素是一个 相同类型的 左括号，那么我们将它从栈中弹出
            并继续处理。否则，这意味着表达式无效。
            4. 如果到最后我们剩下的栈中仍然有元素，那么这意味着表达式无效。
        :param s:
        :return:
        """
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.is_valid('()'))
    print(s.is_valid('()[]{}'))
    print(s.is_valid('(]'))
    print(s.is_valid('([)]'))
    print(s.is_valid('{[]}'))

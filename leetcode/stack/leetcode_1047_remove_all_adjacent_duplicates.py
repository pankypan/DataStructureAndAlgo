class Solution:
    def remove_duplicates(self, S: str) -> str:
        """
        我们可以用栈来维护没有重复项的字母序列：
            若当前的字母和栈顶的字母相同，则弹出栈顶的字母；
            若当前的字母和栈顶的字母不同，则放入当前的字母。
        :param S:
        :return:
        """
        stack = []
        for chr in S:
            if stack and chr == stack[-1]:
                stack.pop()
            else:
                stack.append(chr)
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    res = s.remove_duplicates('abbaca')
    print(res)

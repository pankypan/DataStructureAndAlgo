class Solution:
    def to_lower_case(self, s: str) -> str:
        """
        核心： 利用大小写字符ASCII值相差32的特性转换，主要调用
            chr() -- 将ASCII值转换位字符
            ord() -- 获取字符的ASCII值
        :param s:
        :return:
        """
        lower_char_lis = []
        for char in s:
            if ord('A') <= ord(char) <= ord('Z'):
                char = chr(ord(char) + 32)
                lower_char_lis.append(char)
            else:
                lower_char_lis.append(char)
        return ''.join(lower_char_lis)


if __name__ == '__main__':
    s = Solution()
    print(s.to_lower_case('Hello'))
    print(s.to_lower_case('here'))
    print(s.to_lower_case('LOVELY'))

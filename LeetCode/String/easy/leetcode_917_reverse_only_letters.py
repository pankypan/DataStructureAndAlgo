class Solution:
    def reverse_only_letters(self, S: str) -> str:
        """
        核心: 双指针、 ASCII表
        :param S:
        :return:
        """
        s_lis = [i for i in S]
        s_length = len(s_lis)
        left_p, right_p = 0, len(S) - 1
        letter_ints = [i for i in range(65, 91)] + [i for i in range(97, 123)]
        while left_p < right_p:
            while ord(s_lis[left_p]) not in letter_ints and left_p < s_length - 1:
                left_p += 1
            while ord(s_lis[right_p]) not in letter_ints and right_p > 0:
                right_p -= 1
            if right_p == 0 or left_p >= right_p:
                return ''.join(s_lis)
            s_lis[left_p], s_lis[right_p] = s_lis[right_p], s_lis[left_p]
            left_p += 1
            right_p -= 1
        return ''.join(s_lis)


if __name__ == '__main__':
    s = Solution()
    print(s.reverse_only_letters("ab-cd"))
    print(s.reverse_only_letters("a-bC-dEf-ghIj"))
    print(s.reverse_only_letters("7_28]"))
    print(s.reverse_only_letters("?6C40E"))

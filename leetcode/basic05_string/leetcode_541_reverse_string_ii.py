class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        """
        基本思想：双指针
        :param s:
        :param k:
        :return:
        """
        s_lis = [char for char in s]
        s_length = len(s_lis)
        base_point = 0
        while base_point < s_length:
            if s_length - base_point >= k:
                self.reverse_sub_item(s_lis, base_point, base_point + k - 1)
            else:
                self.reverse_sub_item(s_lis, base_point, s_length - 1)
            base_point += 2 * k
        return ''.join(s_lis)

    @staticmethod
    def reverse_sub_item(s_lis, l_p, r_p):
        while l_p < r_p:
            s_lis[l_p], s_lis[r_p] = s_lis[r_p], s_lis[l_p]
            l_p += 1
            r_p -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.reverse_str('abcdefg', 2))

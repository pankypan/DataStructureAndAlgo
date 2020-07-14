class Solution:
    def reverse_string(self, s: list) -> None:
        """
        双指针法
            时间复杂度：O(N)。执行了 N/2N/2 次的交换。
            空间复杂度：O(1)，只使用了常数级空间。
        """
        s_length = len(s)
        l_point, r_point = 0, s_length - 1
        while l_point < r_point:
            s[l_point], s[r_point] = s[r_point], s[l_point]
            l_point += 1
            r_point -= 1

    def reverse_string_ii(self, s: list) -> None:
        """
        递归方法
            时间复杂度：O(N)。执行了 N/2N/2 次的交换。
            空间复杂度：O(N)，递归过程中使用的堆栈空间。
        :param s:
        :return:
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


if __name__ == '__main__':
    s = Solution()
    t_s = ["h", "e", "l", "l", "o"]
    s.reverse_string(t_s)
    print(t_s)
    s.reverse_string_ii(t_s)
    print(t_s)
    s.reverse_string(['c', 'b', 'a'])
    s.reverse_string(['p', 'a', 'n', 'k'])

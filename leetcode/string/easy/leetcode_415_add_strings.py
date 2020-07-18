class Solution:
    def add_strings(self, num1: str, num2: str) -> str:
        """
        核心：双指针， 补0的使用
        :param num1:
        :param num2:
        :return:
        """
        i, j = len(num1) - 1, len(num2) - 1

        res = []
        carry = 0
        while i >= 0 or j >= 0 or carry != 0:
            a = num1[i] if i >= 0 else 0
            b = num2[j] if j >= 0 else 0
            carry, temp_sum = divmod(int(a) + int(b) + carry, 10)
            res.insert(0, str(temp_sum))
            i -= 1
            j -= 1
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.add_strings('584', '18'))

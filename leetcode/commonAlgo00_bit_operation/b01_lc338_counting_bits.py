# https://leetcode-cn.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        位运算 + 动态规划
        对于所有的数字，只有两类：
            奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。

            偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，
            所以 1 的个数是不变的。
        :param num:
        :return:
        """
        res = list()
        res.append(0)

        for i in range(1, num + 1):
            # 使用 i & 1 来判断奇偶性，提高效率
            if i & 1 == 0:  # 偶数
                res.append(res[i >> 1])
            else:  # 奇数
                res.append(res[i - 1] + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))
    pass

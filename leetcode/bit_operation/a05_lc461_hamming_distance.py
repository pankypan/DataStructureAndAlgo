# https://leetcode-cn.com/problems/hamming-distance/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        位运算：与、左移
        :param x:
        :param y:
        :return:
        """
        bits = 1
        count = 0
        while bits <= x or bits <= y:
            if bits & x != bits & y:
                count += 1
            bits <<= 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))

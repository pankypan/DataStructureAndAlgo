# https://leetcode-cn.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        假定我们现在就从一个数组中寻找最长公共前缀，那么首先，我们可以将第一个元素设置为基准元素x0
        然后我们只需要依次将基准元素和后面的元素进行比较（假定后面的元素依次为x1,x2,x3....），不断更
        新基准元素，直到基准元素和所有元素都满足最长公共前缀的条件，就可以得到最长公共前缀。
        :param strs:
        :return:
        """
        if len(strs) == 0: return ''
        prefix = strs[0]

        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[: len(prefix) - 1]
        return prefix


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
    pass

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split(' ')])


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take leetcode contest"))

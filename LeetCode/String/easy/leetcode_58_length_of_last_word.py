class Solution:
    def length_of_last_word(self, s: str) -> int:
        s = s.strip(' ')
        last_word = s.split(' ')[-1]
        return len(last_word)


if __name__ == '__main__':
    s = Solution()
    print(s.length_of_last_word('Hello World'))

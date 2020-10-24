class Solution:
    def find_lus_length(self, a: str, b: str) -> int:
        a_length = len(a)
        b_length = len(b)
        if a_length == b_length:
            if a == b:
                return -1
            else:
                return a_length
        else:
            return max(a_length, b_length)


if __name__ == '__main__':
    s = Solution()
    print(s.find_lus_length('abc', 'cbda'))
    print(s.find_lus_length('abc', 'abc'))

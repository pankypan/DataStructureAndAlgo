class Solution:
    def find_132_pattern(self, nums: list) -> bool:
        n_length = len(nums)
        if n_length < 2: return False

        mi = [nums[0]]
        for i in range(1, n_length):
            mi.append(min(nums[i], mi[-1]))
        print(mi)

        stack = []
        for i in range(n_length - 1, -1, -1):
            if nums[i] > mi[i]:
                while stack and mi[i] >= stack[-1]:
                    stack.pop()

                if stack and nums[i] > stack[-1]:
                    print(stack)
                    return True
                stack.append(nums[i])
        print(stack)
        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.find_132_pattern([1, 2, 3, 4]))
    print(s.find_132_pattern([3, 1, 4, 2]))
    print(s.find_132_pattern([1, 0, 1, -4, -3]))

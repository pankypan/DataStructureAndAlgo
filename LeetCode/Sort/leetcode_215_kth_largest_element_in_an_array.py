class Solution:
    def find_kth_largest(self, nums: list, k: int) -> int:
        """维护一个单调递减的栈"""
        length = len(nums)
        ret = None
        stack = []
        for i in nums:
            if not stack:
                stack.append(i)
            elif stack and i <= stack[-1]:
                stack.append(i)
            else:
                while stack and stack[-1] < i:
                    ret = stack.pop()
                    length -= 1
                stack.append(i)
                if length == k:
                    return ret
        while length > k:
            ret = stack.pop()
            length -= 1
        return ret


if __name__ == '__main__':
    s = Solution()
    s.find_kth_largest([3, 2, 1, 5, 6, 4], 2)
    s.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)

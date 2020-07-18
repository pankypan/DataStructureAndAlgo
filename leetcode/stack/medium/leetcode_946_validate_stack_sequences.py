class Solution:
    def validate_stack_sequences(self, pushed: list, popped: list) -> bool:
        stack = [pushed.pop(0)]
        for i in range(len(popped)):
            while not stack or stack[-1] != popped[i]:
                val = pushed.pop(0) if pushed else '#'
                stack.append(val)
                if val == '#':
                    break
            stack.pop()
        return True if not stack else False


if __name__ == '__main__':
    s = Solution()
    print(s.validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(s.validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
    print(s.validate_stack_sequences([1, 0], [1, 0]))

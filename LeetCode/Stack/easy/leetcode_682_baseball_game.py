class Solution:
    def calPoints(self, ops: list) -> int:
        sum_points = 0
        stack = []
        for item in ops:
            if item == '+':
                sum_points += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif item == 'D':
                sum_points += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif item == 'C':
                sum_points -= stack.pop()
            else:
                sum_points += int(item)
                stack.append(int(item))

        return sum_points


if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5", "2", "C", "D", "+"]))
    print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))

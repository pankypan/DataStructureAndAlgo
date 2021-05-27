# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
from typing import List


class Solution:
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        """
        贪心算法： 从最矮到最高视角
        :param people:
        :return:
        """
        res = [None] * (len(people) + 1)
        people = sorted(people, key=lambda obj: obj[0])

        for item in people:
            none_count, cur = 0, 0
            while none_count <= item[1]:
                if res[cur] is None or res[cur][0] == item[0]: none_count += 1
                cur += 1
            res[cur - 1] = item
        return res[:-1]

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        贪心算法： 从最高到最矮视角
        :param people:
        :return:
        """
        res = list()
        # 排序简化算法：根据第一个元素正向排序，根据第二个元素反向排序
        people = sorted(people, key=lambda obj: (-obj[0], obj[1]))

        res.append(None)
        for person in people:
            res.insert(person[1], person)
        res.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
    pass

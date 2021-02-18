class Solution:
    memory_cache = {}  # 使用缓存

    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        ret = [[self.get_item_value(i, j) for j in range(1, i + 1)] for i in range(1, numRows + 1)]
        return ret

    def get_item_value(self, i, j):
        """
        获取第i行，第j列的值
        :param i:
        :param j:
        :return:
        """
        if self.memory_cache.get((i, j)):  # 取缓存
            return self.memory_cache[(i, j)]
        if j == 1 or i == j:
            return 1
        ret = self.get_item_value(i - 1, j - 1) + self.get_item_value(i - 1, j)
        self.memory_cache[(i, j)] = ret  # 载入缓存
        return ret

    def generate_ii(self, numRows: int) -> list:
        """
        递归法
        :param numRows:
        :return:
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        ret = self.generate(numRows - 1) + [[self.get_item_value(numRows, j) for j in range(1, numRows + 1)]]
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.get_item_value(5, 2))
    print(s.get_item_value(5, 3))
    print([s.get_item_value(5, j) for j in range(1, 6)])
    print(s.generate(5))
    print(s.generate(0))
    print(s.generate(1))
    print(s.generate(2))

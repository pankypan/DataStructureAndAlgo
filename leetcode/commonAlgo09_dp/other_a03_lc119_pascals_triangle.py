class Solution:
    memory_cache = {}  # 使用缓存

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

    def getRow(self, rowIndex: int) -> list:
        rowIndex = rowIndex + 1
        if rowIndex == 0:
            return []
        ret = [self.get_item_value(rowIndex, j) for j in range(1, rowIndex + 1)]
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(5))
    print(s.getRow(3))

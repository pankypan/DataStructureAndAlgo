# https://leetcode-cn.com/problems/count-complete-tree-nodes/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes1(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countNodes(self, root: TreeNode) -> int:
        """
        二分查找 + 位运算
            对于最大层数为 hh 的完全二叉树，节点个数一定在 [2^h,2^{h+1}-1]的范围内，可以在该范围内通过二分查找的方式得到完全二叉树的节点个数。

            如何判断第 k 个节点是否存在呢？如果第 k 个节点位于第 h 层，则 k 的二进制表示包含 h+1 位，其中最高位是 1，其余各位从高
            到低表示从根节点到第 k 个节点的路径，0 表示移动到左子节点，1 表示移动到右子节点。通过位运算得到第 k 个节点对应的路径，判断该
            路径对应的节点是否存在，即可判断第 k 个节点是否存在。
        :param root:
        :return:
        """
        if not root: return 0

        # 获取完全二叉树的层数
        level, node = 0, root
        while node and node.left:
            level += 1
            node = node.left

        # 二分查找
        low, high = 1 << level, (1 << (level + 1)) - 1
        while low < high:
            middle = int((high - low + 1) / 2) + low
            if self.exists(root, level, middle):
                low = middle
            else:
                high = middle - 1
        return low

    @staticmethod
    def exists(root: TreeNode, level: int, k: int):
        """
        位运算，判断结点是否存在
        :param root:
        :param level:
        :param k:
        :return:
        """
        bits = 1 << (level - 1)
        node = root
        while node and bits > 0:
            if k & bits > 0:
                node = node.right
            else:
                node = node.left
            bits >>= 1
        return node is not None


if __name__ == '__main__':
    pass

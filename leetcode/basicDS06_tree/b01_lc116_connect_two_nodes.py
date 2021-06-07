# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        self.connect_two_nodes(root.left, root.right)
        return root

    def connect_two_nodes(self, node1: Node, node2: Node):
        # base case
        if not node1 or not node2: return

        # 前序遍历框架
        # 将传入的两个节点连接
        node1.next = node2

        # 连接相同父节点的两个子节点
        self.connect_two_nodes(node1.left, node1.right)
        self.connect_two_nodes(node2.left, node2.right)

        # 连接跨越父节点的两个子节点
        self.connect_two_nodes(node1.right, node2.left)


if __name__ == '__main__':
    pass

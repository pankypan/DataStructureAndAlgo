class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None  # TreeNode
        self.right = None  # TreeNode


class BinarySearchTree:
    def __init__(self):
        self.parent = None

    def search(self, root: TreeNode, val: int) -> TreeNode or None:
        """二叉查找树查找元素"""
        if root is None:
            return None

        if val < root.val:
            # 记录当前节点的父节点
            self.parent = root
            root = self.search(root.left, val)
            return root
        elif val > root.val:
            # 记录当前节点的父节点
            self.parent = root
            root = self.search(root.right, val)
            return root
        else:
            return root

    def insert(self, root: TreeNode, val: int) -> TreeNode:
        """增加新节点"""
        # 由于性质4(没有键值相等的节点)，因此插入之前先判断该值是否存在
        tree_node = self.search(root, val)

        if not tree_node:
            new_node = TreeNode(val)
            if self.parent is None:
                root = new_node
            elif val < self.parent.val:
                self.parent.left = new_node
            elif val > self.parent.val:
                self.parent.right = new_node
        return root

    def delete(self, root: TreeNode, val: int) -> TreeNode:
        pass

    def size(self, root: TreeNode) -> int:
        """获取节点个数"""
        if root is None:
            return 0
        return self.size(root.left) + 1 + self.size(root.right)

    def height(self, root: TreeNode) -> int:
        """获取二叉查找树的高度"""
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return left_height + 1 if left_height > right_height else right_height + 1

    def max_val(self, root: TreeNode) -> int:
        pass

    def min_val(self, root: TreeNode) -> int:
        pass

    def in_order_traverse(self, root: TreeNode):
        if root is None:
            return None
        self.in_order_traverse(root.left)
        print(root.val)
        self.in_order_traverse(root.right)

    def in_order_traverse_no_recursion(self, root: TreeNode):
        pass


if __name__ == "__main__":
    val_lis = [3, 10, 1, 6, 14, 4, 7, 13]
    root = TreeNode(8)

    bst = BinarySearchTree()
    for val in val_lis:
        bst.insert(root, val)

    print(bst.size(root))
    print(bst.height(root))
    bst.in_order_traverse(root)

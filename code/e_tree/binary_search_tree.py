class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None  # TreeNode
        self.right = None  # TreeNode


class BinarySearchTree:
    def __init__(self):
        self.parent = None  # 记录当前节点的父节点

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

    def delete(self, root: TreeNode, val: int) -> TreeNode or None:
        """删除节点"""
        if root is None:
            return root

        # 首先搜索该节点，如果不存在直接返回 root
        o = self.search(root, val)
        if o is None:
            return root
        if o.left is None and o.right is None:  # 情况1：如果该节点为叶子节点，直接删除即可
            if self.parent.left == o:  # o为左节点
                self.parent.left = None
            else:  # o为右节点
                self.parent.right = None
        elif o.right is None:  # 情况2-1：如果该节点只有左子树
            if self.parent.left == o:  # o为左节点
                self.parent.left = o.left
            else:  # o为右节点
                self.parent.right = o.left
        elif o.left is None:  # 情况2-2：如果该节点只有右子树
            if self.parent.left == o:  # o为左节点
                self.parent.left = o.right
            else:  # o为右节点
                self.parent.right = o.right
        else:  # 情况3：该节点既有左子树，又有右子树
            q = o
            s = o.left

            # 转左，然后向右到尽头
            # s指向被删节点的“前驱”
            while s.right is not None:
                q = s
                s = s.right

            o.val = s.val
            if q != o:  # 重接q的右子树
                q.right = s.left
            else:  # 重接q的左子树
                q.left = s.left

        return root

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
        # 校验 root 为空
        if root is None:
            return 0

        # 递归终止条件
        if root.right is None:
            return root.val
        return self.max_val(root.right)

    def min_val(self, root: TreeNode) -> int:
        # 校验 root 为空
        if root is None:
            return 0

        # 递归终止条件
        if root.left is None:
            return root.val
        return self.min_val(root.left)

    def in_order_traverse(self, root: TreeNode):
        if root is None:
            return None
        self.in_order_traverse(root.left)
        print(root.val)
        self.in_order_traverse(root.right)

    @staticmethod
    def in_order_traverse_no_recursion(root: TreeNode):
        res_order_lis = []

        stack = []
        current_node = root
        while current_node is not None or len(stack) > 0:
            # 一直循环到二叉树最左端的叶子结点（current_node 是 None）
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            res_order_lis.append(current_node.val)
            current_node = current_node.right
        return res_order_lis


if __name__ == "__main__":
    val_lis = [3, 10, 1, 6, 14, 4, 7, 13]
    root_node = TreeNode(8)

    bst = BinarySearchTree()
    for int_val in val_lis:
        bst.insert(root_node, int_val)

    print(bst.size(root_node))
    print(bst.height(root_node))
    bst.in_order_traverse(root_node)

    print('max_val', bst.max_val(root_node))
    print('min_val', bst.min_val(root_node))
    print(bst.in_order_traverse_no_recursion(root_node))

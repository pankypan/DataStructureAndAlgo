class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, item_lis: list):
        self.root = TreeNode(item_lis[0])
        self.queue = list()  # 用于二叉树追加结点，记录作用
        self.queue.append(self.root)

        # 实例化结点，并构造二叉树
        for item in item_lis[1:]:
            self.add_node(item)

        # 重置 None 结点
        self.set_none_node_as_none(self.root)

    def add_node(self, item):
        new_node = TreeNode(item)

        cur_node = self.queue[0]

        if cur_node.left is None:
            cur_node.left = new_node
            self.queue.append(new_node)
        else:
            cur_node.right = new_node
            self.queue.append(new_node)
            self.queue.pop(0)

    def set_none_node_as_none(self, root: TreeNode):
        if not root: return

        if root.left and root.left.val is None:
            root.left = None
        if root.right and root.right.val is None:
            root.right = None

        self.set_none_node_as_none(root.left)
        self.set_none_node_as_none(root.right)


class TreeTraversal(object):
    def __init__(self):
        self.ret = list()

    def preorder(self, root: TreeNode):
        if not root: return

        self.ret.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root: TreeNode):
        if not root: return

        self.inorder(root.left)
        self.ret.append(root.val)
        self.inorder(root.right)

    def postorder(self, root: TreeNode):
        if not root: return

        self.postorder(root.left)
        self.postorder(root.right)
        self.ret.append(root.val)

    def pre_traversal(self, root: TreeNode):
        self.ret.clear()

        node = root
        if node is None: return
        stack = [node]
        while stack:
            self.ret.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            node = stack.pop()
        return self.ret

    def in_traversal(self, root: TreeNode):
        self.ret.clear()
        stack = []
        pos = root
        while pos is not None or stack:
            if pos is not None:
                stack.append(pos)
                pos = pos.left
            else:
                pos = stack.pop()
                self.ret.append(pos.val)
                pos = pos.right
        return self.ret

    def post_traversal(self, root: TreeNode):
        """
        后序打印二叉树（非递归）
        使用两个栈结构
        第一个栈进栈顺序：左节点->右节点->跟节点(?应该是根-左-右？根结点先进栈再出栈，然后左右子节点入栈？）
        第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
        第二个栈存储为第一个栈的每个弹出依次进栈
        最后第二个栈依次出栈
        :return:
        """
        self.ret.clear()
        node = root
        stack = [node]
        stack2 = []
        while stack:
            node = stack.pop()
            stack2.append(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        while stack2:
            self.ret.append(stack2.pop().val)
        return self.ret

    def level_traversal(self, root: TreeNode):
        self.ret.clear()

        node = root
        if node is None: return
        queue = [node]
        while queue:
            node = queue.pop(0)
            # print(node.val)
            self.ret.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return self.ret


if __name__ == '__main__':
    traversal = TreeTraversal()

    b_tree = BinaryTree([1, 2, None, 4])
    print(traversal.level_traversal(b_tree.root))


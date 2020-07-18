class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self.queue = []  # 用于二叉树追加结点，记录作用

    def add(self, item):
        """
        按层序方式给二叉树追加结点，形成完全二叉树
        :param item:
        :return:
        """
        new_node = TreeNode(item)
        if self.root is None:
            self.root = new_node
            self.queue.append(self.root)
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = new_node
                self.queue.append(tree_node.left)
            else:
                tree_node.right = new_node
                self.queue.append(tree_node.right)
                self.queue.pop(0)

    def pre_traversal_recursion(self):
        """
        前序遍历，递归
        :return:
        """
        ret = []

        def traversal(node):
            if not node: return
            ret.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(self.root)
        return ret

    def in_traversal_recursion(self):
        """
        中序遍历，递归
        :return:
        """
        ret = []

        def traversal(root):
            if not root: return
            traversal(root.left)
            ret.append(root.val)
            traversal(root.right)
        traversal(self.root)
        return ret

    def post_traversal_recursion(self):
        """
        后序遍历，递归
        :return:
        """
        ret = []

        def traversal(root):
            if not root: return
            traversal(root.left)
            traversal(root.right)
            ret.append(root.val)
        traversal(self.root)
        return ret

    def pre_traversal(self):
        ret = []
        node = self.root
        if node is None: return
        stack = [node]
        while stack:
            ret.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            node = stack.pop()
        print(ret)
        return ret

    def in_traversal(self):
        ret = []
        stack = []
        pos = self.root
        while pos is not None or stack:
            if pos is not None:
                stack.append(pos)
                pos = pos.left
            else:
                pos = stack.pop()
                # print(pos.val)
                ret.append(pos.val)
                pos = pos.right
        print(ret)
        return ret

    def post_traversal(self):
        """
        后序打印二叉树（非递归）
        使用两个栈结构
        第一个栈进栈顺序：左节点->右节点->跟节点(?应该是根-左-右？根结点先进栈再出栈，然后左右子节点入栈？）
        第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
        第二个栈存储为第一个栈的每个弹出依次进栈
        最后第二个栈依次出栈
        :return:
        """
        ret = []
        node = self.root
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
            # print(stack2.pop().val)
            ret.append(stack2.pop().val)
        print(ret)
        return ret

    def level_traversal(self):
        ret = []
        node = self.root
        if node is None: return
        queue = [node]
        while queue:
            node = queue.pop(0)
            # print(node.val)
            ret.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(ret)
        return ret


if __name__ == '__main__':
    b_tree = BinaryTree(None)
    for i in [1, 2, 3, 4, 5, 6, 7]:
        b_tree.add(i)
    b_tree.pre_traversal_recursion()
    b_tree.pre_traversal()
    b_tree.in_traversal_recursion()
    b_tree.in_traversal()
    b_tree.post_traversal_recursion()
    b_tree.post_traversal()
    b_tree.level_traversal()

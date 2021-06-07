# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if not root:
            return

        # 1.将root的左子树和右子树拉平。
        self.flatten(root.left)
        self.flatten(root.right)

        # 2.左右子树已经被拉平成一条链表, 将左子树作为右子树
        left = root.left
        right = root.right

        root.left = None
        root.right = left

        # 3.将原先的右子树接到当前右子树的末端
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = right


if __name__ == '__main__':
    pass

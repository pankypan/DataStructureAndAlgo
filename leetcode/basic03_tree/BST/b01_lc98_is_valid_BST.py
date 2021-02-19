# https://leetcode-cn.com/problems/validate-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_bst(root, float('-INF'), float('INF'))

    def check_bst(self, root: TreeNode, min_val, max_val) -> bool:
        if root is None:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        return self.check_bst(root.left, min_val, root.val) and self.check_bst(root.right, root.val, max_val)


if __name__ == '__main__':
    pass

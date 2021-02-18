"""
https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
leetcode 430 medium
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudo_head = Node(None, None, head, None)
        self.flatten_dfs(pseudo_head, head)

        # detach the pseudo head from the real head
        pseudo_head.next.prev = None
        return pseudo_head.next

    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        temp_next = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, temp_next)

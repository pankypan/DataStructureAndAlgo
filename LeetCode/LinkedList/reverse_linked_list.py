class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        print(self)
        # prev = None
        # cur = head
        prev, cur = None, head
        while cur:
            # temp = cur.next
            # cur.next = prev
            # prev = cur
            # cur = temp
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverse_list_II(self, head:ListNode) -> ListNode:
        """Use recursion"""
        if not head or not head.next:
            return head
        N = self.reverse_list_II(head.next)
        head.next.next = head
        head.next = None
        return N

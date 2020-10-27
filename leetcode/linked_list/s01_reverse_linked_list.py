"""
https://leetcode-cn.com/problems/reverse-linked-list/
leetcode 206 easy
"""
from linked_list.common_functions import ListNode


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

    def reverse_list_II(self, head: ListNode) -> ListNode:
        """Use recursion"""
        if not head or not head.next:
            return head
        N = self.reverse_list_II(head.next)
        head.next.next = head
        head.next = None
        return N


if __name__ == "__main__":
    pass

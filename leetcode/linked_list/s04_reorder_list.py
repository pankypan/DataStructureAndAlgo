"""
https://leetcode-cn.com/problems/reorder-list/
leetcode 143 medium
"""
from linked_list.common_functions import ListNode


class Solution:
    @staticmethod
    def find_middle_node(head: ListNode) -> ListNode:
        slow_p, fast_p = head, head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        return slow_p

    @staticmethod
    def reverse_linked_list(head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        pre_p, cur_p = None, head
        nex_p = cur_p.next

        while cur_p:
            cur_p.next = pre_p
            pre_p = cur_p
            cur_p = nex_p
            nex_p = cur_p.next if cur_p else None
        return pre_p

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return

        # step 1: find middle
        middle_head = self.find_middle_node(head)

        # step 2: reverse second half
        rv_head = self.reverse_linked_list(middle_head)

        # step 3: merge list
        cur_1 = head
        cur_2 = rv_head
        if cur_1 is cur_2: return
        while cur_1:
            if cur_1.next is middle_head:
                cur_1.next = None

            temp = cur_1.next
            temp2 = cur_2.next

            cur_1.next = cur_2
            cur_2.next = temp if temp else cur_2.next

            cur_1 = temp
            cur_2 = temp2

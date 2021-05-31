# https://leetcode-cn.com/problems/linked-list-cycle/
from basicDS03_linked_list.common_functions import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """核心：快慢指针"""
        if not head:
            return False

        slow_p, fast_p = head, head
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next

            if fast_p is slow_p:
                return True
        return False

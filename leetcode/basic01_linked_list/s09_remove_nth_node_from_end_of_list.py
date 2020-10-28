"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
leetcode 19 medium
"""
from basic01_linked_list.common_functions import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """核心：快慢指针 + 使用 dumpy 结点"""
        dumpy = ListNode(None)
        slow_p = fast_p = dumpy
        dumpy.next = head

        # fast_p 先走 n 步
        step = 0
        while step < n:
            fast_p = fast_p.next
            step += 1

        # fast_p 和 slow_p 同时走， fast_p 走到尾部结点
        while fast_p.next:
            fast_p = fast_p.next
            slow_p = slow_p.next

        # 删除倒数第 n 个结点
        temp = slow_p.next
        slow_p.next = temp.next
        temp.next = None
        return dumpy.next


if __name__ == "__main__":
    pass

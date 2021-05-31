# https://leetcode-cn.com/problems/reverse-linked-list/
from basicDS03_linked_list.common_functions import ListNode


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        """核心: 递归"""
        if not head or not head.next:
            return head
        n = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return n

    def reverseList(self, head: ListNode) -> ListNode:
        """核心：三指针"""
        if not head:
            return head

        prev, cur, nex = None, head, head.next
        while cur:
            # 翻转单个结点
            cur.next = prev

            # 移动三个指针
            # prev = cur
            # cur = nex
            # nex = nex.next if nex else None
            prev, cur, nex = cur, nex, nex.next if nex else None
        return prev


if __name__ == "__main__":
    pass

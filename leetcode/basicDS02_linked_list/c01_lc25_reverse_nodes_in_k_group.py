# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
from basicDS02_linked_list.common_functions import ListNode


class Solution:
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head

        while prev != tail:
            nex = p.next
            p.next = prev

            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dump = ListNode(0)
        dump.next = head
        pre = dump

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dump.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return dump.next


if __name__ == "__main__":
    pass

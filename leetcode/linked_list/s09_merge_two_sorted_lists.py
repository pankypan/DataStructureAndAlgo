"""
https://leetcode-cn.com/problems/merge-two-sorted-lists/
leetcode 21 easy
"""
from linked_list.common_functions import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 设置dummy 结点, 便于记录
        pre_head = ListNode(None)

        cur = pre_head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        cur.next = l1 or l2
        return pre_head.next


if __name__ == "__main__":
    pass

"""
https://leetcode-cn.com/problems/swap-nodes-in-pairs/
leetcode 24 medium
"""
from basic01_linked_list.common_functions import ListNode, get_linked_list


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """核心：三个指针 pre, cur, nex"""
        if not head:
            return head

        recorder_node = ListNode(None)
        recorder_node.next = head

        pre, cur, nex = recorder_node, head, head.next
        while cur and nex:
            # swap nodes
            cur.next = nex.next
            nex.next = cur
            pre.next = nex

            # move point
            pre = cur
            cur = cur.next
            nex = cur.nex if cur else None
        return recorder_node.next


if __name__ == "__main__":
    pass

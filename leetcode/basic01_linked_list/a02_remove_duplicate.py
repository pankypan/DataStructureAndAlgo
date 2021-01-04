"""
https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
面试题 02.01 easy
"""
from basic01_linked_list.common_functions import ListNode, get_linked_list


class Solution:
    def remove_duplicate(self, head):
        """核心：递归法"""
        if head is None:
            return head
        h_node = self.remove_duplicate(head.next)
        head.next = h_node

        pre_p = head
        p = head.next
        while p:
            if p.val == head.val:
                pre_p.next = p.next
                p.next = None
                p = pre_p.next
                continue
            pre_p = pre_p.next
            p = p.next
        return head

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        """核心：dict"""
        recorder_dict = {}
        if not head:
            return head

        pre, cur = ListNode(None), head
        pre.next = cur
        while cur:
            if recorder_dict.get(cur.val):
                temp = cur.next
                cur.next = None
                pre.next = temp

                cur = temp
                continue
            else:
                recorder_dict[cur.val] = cur

            pre = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicateNodes(get_linked_list([1, 2, 3, 3, 2, 1]))


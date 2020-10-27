"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
leetcode 83 easy
"""
from linked_list.common_functions import ListNode, get_linked_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                if cur.next.next:
                    temp = cur.next.next
                    cur.next.next = None
                    cur.next = temp
                else:
                    cur.next = None
                continue
            cur = cur.next
        return head


if __name__ == "__main__":
    s = Solution()
    s.deleteDuplicates(get_linked_list([1, 1, 2]))

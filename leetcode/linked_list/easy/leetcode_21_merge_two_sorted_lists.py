# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_1 = l1
        cur_2 = l2

        while True:
            if cur_2.val <= cur_1.val:
                if cur_2.next.val <= cur_1.val:
                    cur_2 = cur_2.next
                else:
                    pass
            else:
                pass
        pass
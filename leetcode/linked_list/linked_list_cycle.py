class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # set two cursor--a fast && a slow
        cur_fast, cur_slow = head, head

        while cur_slow and cur_fast:
            cur_slow = cur_slow.next
            try:
                cur_fast = cur_fast.next.next
            except AttributeError:
                return False
            
            # the fast cursor meet the slow cursor
            if cur_fast == cur_slow:
                return True
        return False


node_1 = ListNode(3)
node_2 = ListNode(2)
node_3 = ListNode(0)
node_4 = ListNode(-4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2
s = Solution()
res = s.has_cycle(node_1)
print(res)
n1 = ListNode('a')
print(s.has_cycle(n1))

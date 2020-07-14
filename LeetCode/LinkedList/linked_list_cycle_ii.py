class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detect_cycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # set a cursor which begin from the head
        cur = head

        # a dict to record the appearance ListNode
        nodes_dic = {}
        position = 0

        while cur:
            if nodes_dic.get(cur) or nodes_dic.get(cur) == 0:
                return cur
            else:
                nodes_dic[cur] = position
                position += 1
            cur = cur.next
        return cur

    def detect_cycle_II(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pass


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3

s = Solution()
res = s.detect_cycle(node1)
print(res)

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1
print(s.detect_cycle(node1))



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        # create a ListNode to record the head
        record_node = ListNode(self)
        record_node.next = head

        # set a cursor
        cur = record_node
        while cur.next and cur.next.next:
            # set two adjoin cursor which attach to the cur cursor
            a = cur.next
            b = a.next

            # change the node.next
            """
            cur.next = b
            a.next = b.next
            b.next = a
            """
            cur.next, a.next, b.next = b, b.next, a

            # move the cur cursor
            cur = a
        return record_node.next

    def show_linked_list(self, head):
        cur = head
        val_list = []
        while cur:
            val_list.append(str(cur.val))
            cur = cur.next
        return "->".join(val_list)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
print(s.show_linked_list(node1))
s.swap_pairs(node1)
print(s.show_linked_list(node2))


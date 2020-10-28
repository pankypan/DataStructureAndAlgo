class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_linked_list(v_lis: list) -> ListNode:
    lk_list = []
    for v in v_lis:
        lk_list.append(ListNode(v))

    for idx, node in enumerate(lk_list):
        if idx == len(lk_list) - 1:
            break
        node.next = lk_list[idx + 1]
    return lk_list[0]


def read_linked_list(head: ListNode) -> str:
    temp = []
    cur = head
    while cur:
        temp.append(str(cur.val))
        cur = cur.next
    print("->".join(temp))
    return "->".join(temp)

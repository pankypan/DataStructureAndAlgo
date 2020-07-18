"""
    基于单链表
    1) Reverse singly-linked list
    2) Detect cycle in a list
    3) Merge two sorted lists
    4) Remove nth node from the end
    5) Find middle node
"""

from typing import Optional

from .linked_lists import Node


# Reverse singly-linked list
# 单链表反转
# Note that the input is assumed to be a Node, not a linked list.
def reverse(head: Node) -> Optional[Node]:
    reversed_head = None
    current = head
    while current:
        reversed_head, reversed_head.next, current = current, reversed_head, current.next
    return reversed_head


# Detect cycle in a list
# 检测环
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Merge two sorted linked list
# 有序链表合并
def merge_sorted_list(l1: Node, l2: Node) -> Optional[Node]:
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None)
        current = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        current.next = p1 if p1 else p2
        return fake_head.next_node
    return l1 or l2


# Remove nth node from the end
# 删除倒数第n个节点。假设n大于0
def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
    fast = head
    count = 0
    while fast and count < n:
        fast = fast.next
        count += 1
    if not fast and count < n:  # not that many nodes
        return head
    if not fast and count == n:
        return head.next_node

    slow = head
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return head


# Find the middle node of this linked_list
# 找到中间结点
def find_middle_node(head: Node) -> Optional[Node]:
    slow, fast = head, head
    fast = fast.next_node if fast else None
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow

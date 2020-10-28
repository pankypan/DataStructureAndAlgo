"""
https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
leetcode 430 medium
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        pass

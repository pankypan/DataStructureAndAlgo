# https://leetcode-cn.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        双指针
        :param head:
        :return:
        """
        # 将数据元素装入列表中
        data_lis = list()
        node = head
        while node:
            data_lis.append(node.val)
            node = node.next

        # 双指针, 判断列表中元素是否为回文
        l_p, r_p = 0, len(data_lis) - 1
        while l_p < r_p:
            if data_lis[l_p] != data_lis[r_p]:
                return False
            l_p += 1
            r_p -= 1
        return True

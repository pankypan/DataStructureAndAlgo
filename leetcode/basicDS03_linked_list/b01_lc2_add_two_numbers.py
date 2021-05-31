# https://leetcode-cn.com/problems/add-two-numbers/
from basicDS03_linked_list.common_functions import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """核心：双指针"""
        res = ListNode(None)
        if not l1 and not l2:
            return res

        carry = 0  # 进位数
        curr, p_l1, p_l2 = res, l1, l2
        while p_l1 or p_l2 or carry:
            x = p_l1.val if p_l1 else 0
            y = p_l2.val if p_l2 else 0
            sum_x_y = x + y + carry
            curr.next = ListNode(sum_x_y % 10)
            curr = curr.next
            carry = sum_x_y // 10

            p_l1 = p_l1.next if p_l1 else None
            p_l2 = p_l2.next if p_l2 else None
        return res.next


if __name__ == "__main__":
    pass

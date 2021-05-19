# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
from basicDS02_linked_list.common_functions import ListNode, get_linked_list


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """使用快慢指针"""
        if not head:
            return head

        slow_p, fast_p = head, head

        i = 1
        while i < k:
            fast_p = fast_p.next
            i += 1

        if i < k - 1:
            return head

        while fast_p.next:
            fast_p = fast_p.next
            slow_p = slow_p.next
        return slow_p


if __name__ == "__main__":
    s = Solution()
    head_1 = get_linked_list([1, 2, 3, 4, 5, 6, 7])
    print(s.getKthFromEnd(head_1, 3).val)

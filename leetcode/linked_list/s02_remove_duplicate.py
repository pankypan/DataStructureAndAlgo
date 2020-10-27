"""
https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
面试题 02.01 easy
"""
from linked_list.common_functions import ListNode, get_linked_list


class Solution:
    @staticmethod
    def remove_duplicate(head: ListNode) -> ListNode:
        """
        两次循环
            时间复杂度：O(N^2)
            空间复杂度: O(1)
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head

        outer_cur = head

        while outer_cur is not None:
            inner_pre = outer_cur
            inner_cur = outer_cur.next
            while inner_cur is not None:
                if outer_cur.val == inner_cur.val:  # 结点值重复
                    inner_pre.next = inner_cur.next
                    temp = inner_cur.next
                    inner_cur.next = None
                    inner_cur = temp
                    continue
                inner_pre = inner_pre.next
                inner_cur = inner_cur.next
            outer_cur = outer_cur.next
        return head

    def remove_duplicate_2(self, head):
        """
        递归法
        :param head:
        :return:
        """
        if head is None:
            return head
        h_node = self.remove_duplicate_2(head.next)
        head.next = h_node

        pre_p = head
        p = head.next
        while p:
            if p.val == head.val:
                pre_p.next = p.next
                p.next = None
                p = pre_p.next
                continue
            pre_p = pre_p.next
            p = p.next
        return head

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        """使用 哈希表 dict"""
        recorder_dict = {}
        if not head:
            return head

        pre, cur = ListNode(None), head
        pre.next = cur
        while cur:
            if recorder_dict.get(cur.val):
                temp = cur.next
                cur.next = None
                pre.next = temp

                cur = temp
                continue
            else:
                recorder_dict[cur.val] = cur

            pre = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicateNodes(get_linked_list([1, 2, 3, 3, 2, 1]))


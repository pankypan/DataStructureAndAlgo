class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


if __name__ == '__main__':
    ll = [1, 3, 1, 4, 5, 5, 7]
    list_node_lis = [ListNode(i) for i in ll]
    for i, node in enumerate(list_node_lis):
        if i == len(ll) - 1:
            break
        node.next = list_node_lis[i + 1]

    hd = list_node_lis[0]
    while hd:
        print(hd.val, end='->')
        hd = hd.next

    solution = Solution()
    hd = solution.remove_duplicate_2(list_node_lis[0])
    print('\n')
    while hd:
        print(hd.val, end='->')
        hd = hd.next

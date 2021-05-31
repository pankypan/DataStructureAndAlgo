class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        排序
            尚未完成
        :param head:
        :return:
        """
        if not head: return head

        temp_lis = [head]
        cur = head.next
        while cur:
            if cur.val >= temp_lis[-1].val:
                temp_lis.append(cur)
            else:
                count = 0
                while cur.val >= temp_lis[count].val:
                    count += 1
                temp_lis.insert(count, cur)
            cur = cur.next

        head = temp_lis[0]
        for index, node in enumerate(temp_lis):
            try:
                node.next = temp_lis[index + 1]
            except IndexError as e:
                node.next = None
        return head


if __name__ == '__main__':
    pass

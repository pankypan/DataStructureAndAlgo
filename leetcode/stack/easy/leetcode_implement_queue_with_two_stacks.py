class CQueue:
    def __init__(self):
        self.a_stack, self.b_stack = [], []

    def append_tail(self, value: int) -> None:
        self.a_stack.append(value)

    def delete_head(self) -> int:
        # 先检查辅助栈 b_stack 是否为空栈，如为空，b_stack 获取主栈a_stack全部元素
        # 若不为空直接从辅助栈 b_stack 删除元素
        if not self.b_stack:
            while self.a_stack:
                self.b_stack.append(self.a_stack.pop())
        return self.b_stack.pop() if self.b_stack else -1


if __name__ == '__main__':
    q = CQueue()
    q.append_tail(1)
    q.append_tail(2)
    print(q.delete_head())
    q.append_tail(3)
    q.append_tail(4)
    print(q.delete_head())
    print(q.delete_head())
    print(q.delete_head())
    print(q.delete_head())

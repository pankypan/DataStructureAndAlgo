class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    @property
    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

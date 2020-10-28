class Queue:
    def __init__(self):
        self.arr = []
        self.front = 0  # 队头
        self.rear = 0  # 队尾

    def is_empty(self):
        return self.front == self.rear

    @property
    def size(self):
        return self.rear - self.front

    def get_front(self):
        if self.is_empty():
            return None
        return self.arr[self.front]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.arr[self.rear - 1]

    def push(self, item):
        self.arr.append(item)
        self.rear += 1

    def pop(self):
        if self.rear > self.front:
            res = self.arr[self.front]
            self.front += 1
            return res
        else:
            print("空队列")
            return None

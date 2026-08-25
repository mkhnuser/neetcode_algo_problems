class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.q = [0] * k

        self.front_pointer = 0
        self.back_pointer = -1

        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.back_pointer = (self.back_pointer + 1) % self.k
        self.q[self.back_pointer] = value
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front_pointer = (self.front_pointer + 1) % self.k
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.front_pointer]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.back_pointer]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

from typing import List


class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Q:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def put(self, item):
        node = Node(item)
        prev_tail = self.tail

        if prev_tail is None:
            self.head = node
        else:
            prev_tail.next = node

        self.tail = node
        self.size += 1

    def get(self):
        prev_head = self.head

        if prev_head is None:
            raise RuntimeError("Q is empty.")

        if prev_head is self.tail:
            self.tail = None

        self.head = prev_head.next
        self.size -= 1
        return prev_head.val

    def peek_head(self):
        if self.head is None:
            raise RuntimeError("Q is empty.")
        return self.head.val

    def peek_tail(self):
        if self.tail is None:
            raise RuntimeError("Q is empty.")
        return self.tail.val


class MyStack:
    def __init__(self):
        self.q = Q()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        for _ in range(self.q.size - 1):
            self.q.put(self.q.get())
        return self.q.get()

    def top(self) -> int:
        return self.q.peek_tail()

    def empty(self) -> bool:
        return self.q.size == 0

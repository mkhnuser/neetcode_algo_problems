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


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # NOTE: sandwiches act as a stack, whereas students are a queue.
        q = Q()

        for student in students:
            q.put(student)

        stack = []

        for sandwich in reversed(sandwiches):
            stack.append(sandwich)

        sandwiches = stack

        c = 0

        while sandwiches:
            if c == q.size:
                return q.size

            sandwich = sandwiches.pop()
            student = q.get()

            if student == sandwich:
                c = 0
                continue
            else:
                q.put(student)
                c += 1
                sandwiches.append(sandwich)

        return 0


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # NOTE: sandwiches act as a stack, whereas students are a queue.
        counter_mapping = {}

        for student in students:
            if student not in counter_mapping:
                counter_mapping[student] = 0
            counter_mapping[student] += 1

        output = len(students)

        for sandwich in sandwiches:
            if counter_mapping.get(sandwich, 0) > 0:
                output -= 1
                counter_mapping[sandwich] -= 1
            else:
                break

        return output

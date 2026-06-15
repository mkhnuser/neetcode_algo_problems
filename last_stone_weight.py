from typing import List


class MinHeap:
    def __init__(self):
        # NOTE: We use zero-based indexing.
        self.data = []

    def push(self, val: int) -> None:
        # NOTE:
        # 1. Append to the end of the heap.
        # 2. Heapify up.

        self.data.append(val)
        self._heapify_up(len(self.data) - 1)

    def pop(self) -> int | None:
        # NOTE:
        # Store the output.
        # Replace the output with the last element.
        # Heapify down.
        # Handle an empty heap and heap of size one edge cases.

        output = None
        if not self.data:
            return output

        output = self.data[0]

        if len(self.data) == 1:
            self.data = []
            return output

        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return output

    def top(self) -> int:
        output = -1
        if not self.data:
            return output

        output = self.data[0]
        return output

    def heapify(self, nums: List[int]) -> None:
        self.data = nums

        for i in reversed(range(0, (len(nums) // 2))):
            self._heapify_down(i)

    def _get_parent_index(self, node_index: int) -> int:
        return (node_index - 1) // 2

    def _get_left_child_index(self, node_index: int) -> int:
        return (node_index * 2) + 1

    def _get_right_child_index(self, node_index: int) -> int:
        return (node_index * 2) + 2

    def _heapify_up(self, node_index: int) -> None:
        if node_index <= 0:
            return

        parent_index = self._get_parent_index(node_index)
        parent_value = self.data[parent_index]
        node_value = self.data[node_index]

        if parent_value > node_value:
            self.data[parent_index], self.data[node_index] = (
                self.data[node_index],
                self.data[parent_index],
            )
            self._heapify_up(parent_index)

    def _heapify_down(self, node_index: int) -> None:
        left_child_index = self._get_left_child_index(node_index)
        right_child_index = self._get_right_child_index(node_index)

        node_value = self.data[node_index]
        min_value_index = node_index

        if (
            left_child_index < len(self.data)
            and self.data[left_child_index] < node_value
        ):
            min_value_index = left_child_index

        if (
            right_child_index < len(self.data)
            and self.data[right_child_index] < self.data[min_value_index]
        ):
            min_value_index = right_child_index

        if min_value_index != node_index:
            self.data[node_index], self.data[min_value_index] = (
                self.data[min_value_index],
                self.data[node_index],
            )
            self._heapify_down(min_value_index)


class Solution:
    def __init__(self) -> None:
        self.min_heap = MinHeap()

    def lastStoneWeight(self, stones: List[int]) -> int:
        # NOTE: Given: [4, 1, 0], compute: [-4, -1, 0].
        self.min_heap.heapify([-w for w in stones])

        while len(self.min_heap.data) >= 2:
            x = self.min_heap.pop()
            y = self.min_heap.pop()
            assert x is not None
            assert y is not None

            maximum = max(x, y)
            minimum = min(x, y)
            new_weight = maximum - minimum
            if new_weight != 0:
                self.min_heap.push(-new_weight)

        if len(self.min_heap.data) == 1:
            return -self.min_heap.top()

        return 0

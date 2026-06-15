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

    def pop(self) -> int:
        # NOTE:
        # Store the output.
        # Replace the output with the last element.
        # Heapify down.
        # Handle an empty heap and heap of size one edge cases.

        output = -1
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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = MinHeap()
        min_heap.heapify([-num for num in nums])

        for _ in range(k - 1):
            min_heap.pop()

        return -min_heap.pop()

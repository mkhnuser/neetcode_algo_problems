from typing import List
from collections import deque


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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # NOTE:
        # 1. Create a max heap to keep track of how many tasks there are.
        # 2. Create a deque which contains (#, t).
        # Where # - is the number of tasks to execute, t is the execution time.

        max_heap = MinHeap()
        count_map = {}

        for task in tasks:
            if task not in count_map:
                count_map[task] = 0
            count_map[task] += 1

        task_counts = list(count_map.values())
        task_counts = [-task_count for task_count in task_counts]
        # NOTE: For example:
        # task_counts = [3, 2, 2].
        # Becomes: [-3, -2, -2], and so min heap allows you to achieve a max heap.
        max_heap.heapify(task_counts)
        d = deque()
        time = 0

        while max_heap.data or d:
            time += 1

            if max_heap.data:
                # NOTE: OK, at this point we say:
                # - This task will be executed at some point in the future.
                task_count = -max_heap.pop()
                task_count -= 1
                if task_count >= 1:
                    d.append((task_count, time + n))
            if d and d[0][1] == time:
                task_count, execution_time = d.popleft()
                max_heap.push(-task_count)

        return time


def test():
    tasks = ["X", "X", "Y", "Y"]
    n = 2
    sol = Solution()
    print(sol.leastInterval(tasks, n))
    tasks = ["A", "A", "A", "B", "C"]
    n = 3
    print(sol.leastInterval(tasks, n))


if __name__ == "__main__":
    test()

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)

        # NOTE: [enqueue time, processing time, original index].

        tasks.sort(reverse=True)
        min_heap = []
        time = 0
        output = []

        while tasks or min_heap:
            while tasks and tasks[-1][0] <= time:
                task = tasks.pop()
                heapq.heappush(min_heap, [task[1], task[2]])

            if not min_heap:
                time = max(time, tasks[-1][0])
            else:
                task = heapq.heappop(min_heap)
                processing_time = task[0]
                output.append(task[1])
                time += processing_time

        return output


def test():
    tasks = [[1, 4], [3, 3], [2, 1]]
    sol = Solution()
    print(sol.getOrder(tasks))


if __name__ == "__main__":
    test()

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mapping = {}

        for time in times:
            u, v, w = time

            if u not in adj_mapping:
                adj_mapping[u] = [(v, w)]
            else:
                adj_mapping[u].append((v, w))

        # NOTE: Store: (distance, node).
        min_heap = []
        heapq.heappush(min_heap, (0, k))
        visited = set()
        time = float("-inf")

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue

            time = max(time, current_distance)

            for neighbor_node, neighbor_weight in adj_mapping.get(current_node, []):
                if neighbor_node not in visited:
                    heapq.heappush(
                        min_heap, (current_distance + neighbor_weight, neighbor_node)
                    )

            visited.add(current_node)

        return time if len(visited) == n else -1


def test() -> None:
    times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
    n = 4
    k = 1
    sol = Solution()
    print(sol.networkDelayTime(times, n, k))


if __name__ == "__main__":
    test()

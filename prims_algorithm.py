import heapq
from typing import List


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj_mapping = {}

        for edge in edges:
            u, v, w = edge

            if u not in adj_mapping:
                adj_mapping[u] = [(v, w)]
            else:
                adj_mapping[u].append((v, w))

            if v not in adj_mapping:
                adj_mapping[v] = [(u, w)]
            else:
                adj_mapping[v].append((u, w))

        start_vertex = 0
        visited = set()
        # NOTE: Store (w, u, v) pairs.
        min_heap = []

        for neighbor_vertex, edge_weight in adj_mapping.get(start_vertex, []):
            heapq.heappush(min_heap, (edge_weight, start_vertex, neighbor_vertex))

        visited.add(start_vertex)
        mst_sum = 0
        mst = set()

        while min_heap:
            w, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            mst_sum += w
            mst.add((u, v))

            for neighbor_vertex, edge_weight in adj_mapping.get(v, []):
                if neighbor_vertex not in visited:
                    heapq.heappush(min_heap, (edge_weight, v, neighbor_vertex))

            visited.add(v)

        return -1 if len(visited) != n else mst_sum


def test() -> None:
    n = 5
    edges = [
        [0, 1, 10],
        [0, 2, 3],
        [1, 3, 2],
        [2, 1, 4],
        [2, 3, 8],
        [2, 4, 2],
        [3, 4, 5],
    ]
    sol = Solution()
    print(sol.minimumSpanningTree(n, edges))


if __name__ == "__main__":
    test()

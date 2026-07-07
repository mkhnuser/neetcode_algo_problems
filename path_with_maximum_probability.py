import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # NOTE: Given n, you have nodes 0 .. n - 1.
        adj_mapping = {}

        for i, edge in enumerate(edges):
            u, v = edge
            prob = succProb[i]

            if u not in adj_mapping:
                adj_mapping[u] = [(v, prob)]
            else:
                adj_mapping[u].append((v, prob))

            if v not in adj_mapping:
                adj_mapping[v] = [(u, prob)]
            else:
                adj_mapping[v].append((u, prob))

        # NOTE: Objective: find max path which starts at start_node end ends with end_node.
        # If this path can be found, return its length.
        # If this path is not present, return 0.
        distances = {}
        min_heap = []  # NOTE: Store (dist, node).
        heapq.heappush(min_heap, (-1, start_node))

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            dist *= -1

            if node in distances:
                continue

            for neighbor, prob in adj_mapping.get(node, []):
                if neighbor not in distances:
                    heapq.heappush(min_heap, (-(dist * prob), neighbor))

            distances[node] = dist

        if end_node not in distances:
            return 0
        return distances[end_node]


def test() -> None:
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    sol = Solution()
    print(sol.maxProbability(n, edges, succProb, start, end))
    print(
        sol.maxProbability(
            **dict(
                n=3,
                edges=[[0, 1], [1, 2], [0, 2]],
                succProb=[0.5, 0.5, 0.3],
                start_node=0,
                end_node=2,
            )
        )
    )
    print(
        sol.maxProbability(
            **dict(n=3, edges=[[0, 1]], succProb=[0.5], start_node=0, end_node=2)
        )
    )


if __name__ == "__main__":
    test()

import math
import heapq
from typing import Dict, List


# NOTE: A simple linear scan solution.
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # NOTE: Given n, 2 <= n <= 100.
        # Vertices are marked from 0 to n - 1.
        adj_mapping = {}

        for edge in edges:
            u, v, w = edge

            if u not in adj_mapping:
                adj_mapping[u] = [(v, w)]
            else:
                adj_mapping[u].append((v, w))

        visited = [False for _ in range(n)]
        distances = [float("+inf") for _ in range(n)]
        distances[src] = 0

        while True:
            c = self.find_current(distances, visited)

            if c is None:
                break

            for n, w in adj_mapping.get(c, []):
                if distances[n] > distances[c] + w:
                    distances[n] = distances[c] + w

            visited[c] = True

        # NOTE: There is no guarantee that a graph is connected.
        distances = [d if not math.isinf(d) else -1 for d in distances]
        output_mapping = {}
        for v, dist in enumerate(distances):
            output_mapping[v] = dist
        return output_mapping

    def find_current(self, distances: List, visited: List) -> int | None:
        c = None
        min_dist = float("+inf")

        for v, distance in enumerate(distances):
            if distance < min_dist and not visited[v]:
                min_dist = distance
                c = v

        return c


# NOTE: A min heap solution.
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # NOTE: Given n, 2 <= n <= 100.
        # Vertices are marked from 0 to n - 1.
        adj_mapping = {}

        for edge in edges:
            u, v, w = edge

            if u not in adj_mapping:
                adj_mapping[u] = [(v, w)]
            else:
                adj_mapping[u].append((v, w))

        # NOTE: Store (distance, node) pairs.
        min_heap: list[tuple[int | float, int]] = []
        heapq.heappush(min_heap, (0, src))
        output_mapping = {}

        while min_heap:
            current_tuple = self.find_current_tuple(min_heap)

            if current_tuple is None:
                break

            c_w, c = current_tuple

            if c in output_mapping:
                # NOTE: The best distance has already been calculated;
                # We don't want to overwrite it with stale values.
                continue

            for n_n, n_w in adj_mapping.get(c, []):
                if n_n not in output_mapping:
                    heapq.heappush(min_heap, (c_w + n_w, n_n))

            output_mapping[c] = c_w

        # NOTE: There is no guarantee that a graph is connected.
        for v in range(n):
            if v not in output_mapping:
                output_mapping[v] = -1
        return output_mapping

    def find_current_tuple(self, min_heap: list) -> tuple[int, int] | None:
        try:
            w, c = heapq.heappop(min_heap)
        except IndexError:
            return None

        return w, c

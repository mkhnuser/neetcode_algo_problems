import heapq
from typing import List


NEIGHBOR_DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        grid = heights
        n = len(grid)
        m = len(grid[0])

        min_heap = []
        start_vertex = (0, 0)
        end_vertex = (n - 1, m - 1)
        heapq.heappush(
            min_heap,
            (0, start_vertex),
        )  # NOTE: Store (effort, vertex) pairs.
        visited = set()

        while min_heap:
            current_effort, current_vertex = heapq.heappop(min_heap)

            if current_vertex in visited:
                continue

            if current_vertex == end_vertex:
                return current_effort

            for neighbor_vertex, neighbor_height in self.get_neighbors(
                current_vertex[0],
                current_vertex[1],
                n,
                m,
                grid,
            ):
                if neighbor_vertex not in visited:
                    current_height = grid[current_vertex[0]][current_vertex[1]]
                    edge_cost = abs(current_height - neighbor_height)
                    new_effort = max(current_effort, edge_cost)
                    heapq.heappush(
                        min_heap,
                        (new_effort, neighbor_vertex),
                    )

            visited.add(current_vertex)

    def get_neighbors(
        self,
        i: int,
        j: int,
        n: int,
        m: int,
        grid: List[List[int]],
    ) -> tuple[tuple[tuple[int, int], int]]:
        # NOTE: Return a tuple of tuples of the form (point coords, elevation).
        neighbors = []

        for direction in NEIGHBOR_DIRECTIONS:
            i_incr, j_incr = direction
            next_i, next_j = i + i_incr, j + j_incr
            if 0 <= next_i < n and 0 <= next_j < m:
                neighbors.append(((next_i, next_j), grid[next_i][next_j]))

        return tuple(neighbors)

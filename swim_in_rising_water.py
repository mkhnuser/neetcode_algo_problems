import heapq
from typing import List


# NOTE: Only move allow moves to the right or to the bottom.
NEIGHBOR_DIRECTIONS = (
    (0, +1),
    (+1, 0),
    (0, -1),
    (-1, 0),
)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        start_vertex = (0, 0)
        end_vertex = (n - 1, m - 1)
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], start_vertex))
        visited = set()

        while min_heap:
            dist, vertex = heapq.heappop(min_heap)

            if vertex in visited:
                continue

            if vertex == end_vertex:
                return dist

            neighbors = self.get_neighbors(
                vertex[0],
                vertex[1],
                n,
                m,
                grid,
            )
            for neighbor, elevation in neighbors:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (max(elevation, dist), neighbor))

            visited.add(vertex)

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


def test() -> None:
    grid = [[0, 1], [2, 3]]
    sol = Solution()
    print(sol.swimInWater(grid))
    grid = [[0, 1, 2, 10], [9, 14, 4, 13], [12, 3, 8, 15], [11, 5, 7, 6]]
    sol = Solution()
    print(sol.swimInWater(grid))


if __name__ == "__main__":
    test()

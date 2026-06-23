from typing import List
from queue import Queue


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        i = 0
        j = 0
        visited = set()
        return self.count_with_bfs(grid, n, m, i, j, visited)

    def count_with_bfs(
        self,
        grid: List[List[int]],
        n: int,
        m: int,
        i: int,
        j: int,
        visited: set[tuple[int, int]],
    ) -> int:
        dist = 0
        q = Queue()
        q.put((i, j, dist))

        while q.qsize():
            i, j, dist = q.get()

            if (
                i < 0
                or j < 0
                or i >= n
                or j >= m
                or (i, j) in visited
                or grid[i][j] == 1
            ):
                continue

            visited.add((i, j))

            if i == (n - 1) and j == (m - 1):
                return dist

            for dir in DIRECTIONS:
                i_incr, j_incr = dir
                q.put((i + i_incr, j + j_incr, dist + 1))

        return -1

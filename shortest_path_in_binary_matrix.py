from typing import List
from queue import Queue


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
    (+1, +1),  # upper-right
    (+1, -1),  # lower-right
    (-1, -1),  # lower-left
    (-1, +1),  # upper-left
)


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.solve_with_bfs(grid)

    def solve_with_bfs(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        dist = 1
        q = Queue()
        q.put((0, 0, dist))
        visited = set()
        visited.add((0, 0))

        while q.qsize() > 0:
            i, j, dist = q.get()

            if i == (n - 1) and j == (n - 1):
                return dist

            for dir in DIRECTIONS:
                i_incr, j_incr = dir
                next_i = i + i_incr
                next_j = j + j_incr

                if (next_i, next_j) in visited:
                    continue

                if (
                    next_i < 0
                    or next_i >= n
                    or next_j < 0
                    or next_j >= m
                    or grid[next_i][next_j] == 1
                ):
                    continue

                q.put((next_i, next_j, dist + 1))
                visited.add((next_i, next_j))

        return -1

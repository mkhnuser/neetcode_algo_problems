from typing import List
from queue import Queue


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # NOTE:
        # 0 is empty.
        # 1 is fresh.
        # 2 is rotten.
        if not grid:
            return -1

        n = len(grid)
        m = len(grid[0])

        dist = 0
        q = Queue()
        visited = set()

        num_of_fresh = 0
        for row in grid:
            for item in row:
                if item == 1:
                    num_of_fresh += 1

        if num_of_fresh == 0:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put((i, j, dist))
                    visited.add((i, j))

        return self.bfs(grid, n, m, q, visited, num_of_fresh)

    def bfs(
        self,
        grid: List[List[int]],
        n: int,
        m: int,
        q: Queue,
        visited: set[tuple[int, int]],
        num_of_fresh: int,
    ) -> int:
        rotten_fresh_fruit = 0

        while q.qsize() > 0:
            i, j, dist = q.get()

            if grid[i][j] == 1:
                rotten_fresh_fruit += 1

            if rotten_fresh_fruit == num_of_fresh:
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
                    or grid[next_i][next_j] == 0
                ):
                    continue

                q.put((next_i, next_j, dist + 1))
                visited.add((next_i, next_j))

        return -1

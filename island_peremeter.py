from typing import List
from queue import Queue


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # NOTE:
        # 1 = land;
        # 0 = water.

        # return self.brute_force(grid)
        return self.solve_with_bfs(grid)

    def brute_force(self, grid: List[List[int]]) -> int:
        p = 0

        if not any(list_ for list_ in grid):
            return p

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue

                for dir in DIRECTIONS:
                    i_incr, j_incr = dir
                    if self.is_water(i + i_incr, j + j_incr, n, m, grid):
                        p += 1

        return p

    def is_water(self, i: int, j: int, n: int, m: int, grid: List[List[int]]) -> bool:
        if i >= n or i < 0 or j >= m or j < 0:
            return True
        if grid[i][j] == 0:
            return True
        return False

    def solve_with_dfs(self, grid: List[List[int]]) -> int:
        p = 0
        if not any(list_ for list_ in grid):
            return p

        n = len(grid)
        m = len(grid[0])

        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return self.dfs(i, j, n, m, grid, visited)

    def dfs(
        self,
        i: int,
        j: int,
        n: int,
        m: int,
        grid: List[List[int]],
        visited: set[tuple[int, int]],
    ) -> int:
        if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visited:
            return 0

        visited.add((i, j))

        p = 0
        for dir in DIRECTIONS:
            i_incr, j_incr = dir
            p += self.dfs(i + i_incr, j + j_incr, n, m, grid, visited)

        return p

    def solve_with_bfs(self, grid: List[List[int]]) -> int:
        p = 0
        if not any(list_ for list_ in grid):
            return p

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return self.bfs(i, j, n, m, grid)

    def bfs(
        self,
        i: int,
        j: int,
        n: int,
        m: int,
        grid: List[List[int]],
    ) -> int:
        q = Queue()
        q.put((i, j))
        visited = set()
        p = 0

        while q.qsize():
            i, j = q.get()

            if (i, j) in visited:
                continue

            if self.is_water(i, j, n, m, grid):
                p += 1
                continue

            visited.add((i, j))

            for dir in DIRECTIONS:
                i_incr, j_incr = dir
                q.put((i + i_incr, j + j_incr))

        return p

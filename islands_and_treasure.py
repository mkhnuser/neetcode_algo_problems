from typing import List
from queue import Queue


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)
OK_CELL = 2147483647


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # NOTE:
        # -1 can't be traversed.
        # 0 - a chest.
        # 2147483647 - a land. If can't be traversed, let it remain as is.
        # Modify in-place.
        if not grid:
            return

        q = Queue()
        dist = 0
        visited = set()

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.put((i, j, dist))
                    visited.add((i, j))

        while q.qsize() > 0:
            i, j, dist = q.get()
            grid[i][j] = dist

            for dir in DIRECTIONS:
                i_incr, j_incr = dir
                i_next, j_next = i + i_incr, j + j_incr

                if (
                    0 <= i_next < n
                    and 0 <= j_next < m
                    and (i_next, j_next) not in visited
                    and grid[i_next][j_next] == OK_CELL
                ):
                    q.put((i_next, j_next, dist + 1))
                    visited.add((i_next, j_next))


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # NOTE:
        # -1 can't be traversed.
        # 0 - a chest.
        # 2147483647 - a land. If can't be traversed, let it remain as is.
        # Modify in-place.
        if not grid:
            return

        n = len(grid)
        m = len(grid[0])
        visited: set[tuple[int, int]] = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == OK_CELL:
                    grid[i][j] = self.dfs(i, j, n, m, grid, visited)

    def dfs(
        self,
        i: int,
        j: int,
        n: int,
        m: int,
        grid: List[List[int]],
        visited: set[tuple[int, int]],
    ) -> int:
        if (
            (i < 0 or i >= n)
            or (j < 0 or j >= m)
            or ((i, j) in visited)
            or grid[i][j] == -1
        ):
            return OK_CELL

        if grid[i][j] == 0:
            return 0

        visited.add((i, j))

        # NOTE: Try to minimize the distance to the chest.
        dist = OK_CELL

        for dir in DIRECTIONS:
            i_incr, j_incr = dir
            next_i = i + i_incr
            next_j = j + j_incr

            dist = min(dist, 1 + self.dfs(next_i, next_j, n, m, grid, visited))

        visited.remove((i, j))
        return dist

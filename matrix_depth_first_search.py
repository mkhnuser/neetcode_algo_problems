from typing import List


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        i = 0
        j = 0
        visited = set()
        return self.recurse_counting(grid, n, m, i, j, visited)

    def recurse_counting(
        self,
        grid: List[List[int]],
        n: int,
        m: int,
        i: int,
        j: int,
        visited: set[tuple[int, int]],
    ) -> int:
        if i < 0 or j < 0 or i >= n or j >= m or (i, j) in visited or grid[i][j] == 1:
            return 0
        if i == (n - 1) and j == (m - 1):
            return 1

        visited.add((i, j))

        counter = 0
        for dir in DIRECTIONS:
            i_incr, j_incr = dir
            counter += self.recurse_counting(
                grid,
                n,
                m,
                i + i_incr,
                j + j_incr,
                visited,
            )

        visited.remove((i, j))
        return counter

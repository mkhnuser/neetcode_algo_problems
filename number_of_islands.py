from typing import List
from collections import deque


ISLAND_MARK = "1"
WATER_MARK = "0"
DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


def visit_dfs(grid, n, m, i, j, visited_matrix):
    """Marks one contiguous island as a visited island."""
    if (
        i < 0
        or i >= n
        or j < 0
        or j >= m
        or visited_matrix[i][j]
        or grid[i][j] == WATER_MARK
    ):
        return None

    visited_matrix[i][j] = True
    for direction in DIRECTIONS:
        i_incr, j_incr = direction
        visit_dfs(grid, n, m, i + i_incr, j + j_incr, visited_matrix)


def visit_bfs(grid, n, m, i, j, visited_matrix):
    """Marks one contiguous island as a visited island."""
    d = deque()
    d.append((i, j))

    while d:
        c = d.popleft()
        i, j = c

        if (
            i < 0
            or i >= n
            or j < 0
            or j >= m
            or visited_matrix[i][j]
            or grid[i][j] == WATER_MARK
        ):
            continue

        visited_matrix[i][j] = True

        for direction in DIRECTIONS:
            i_incr, j_incr = direction
            d.append((i + i_incr, j + j_incr))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        visited_matrix = [[False for _ in range(m)] for __ in range(n)]
        island_counter = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == ISLAND_MARK and not visited_matrix[i][j]:
                    visit_bfs(grid, n, m, i, j, visited_matrix)
                    island_counter += 1

        return island_counter


def test():
    grid = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    sol = Solution()
    print(sol.numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    sol = Solution()
    print(sol.numIslands(grid))


if __name__ == "__main__":
    test()

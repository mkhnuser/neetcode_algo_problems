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
        # 0 is the empty cell.
        # 1 is fresh; 2 is rotten.
        if not grid:
            return -1

        n = len(grid)
        m = len(grid[0])

        num_of_fresh = 0
        q = Queue()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    num_of_fresh += 1
                if grid[i][j] == 2:
                    q.put((i, j, 0))
                    visited.add((i, j))

        if num_of_fresh == 0:
            return 0

        if not q:
            return -1

        num_of_rotten = 0

        while q.qsize() > 0:
            i, j, dist = q.get()

            if grid[i][j] == 1:
                num_of_rotten += 1

            if num_of_rotten == num_of_fresh:
                return dist

            for dir in DIRECTIONS:
                i_incr, j_incr = dir
                next_i, next_j = i + i_incr, j + j_incr

                if (
                    (0 <= next_i < n)
                    and (0 <= next_j < m)
                    and (next_i, next_j) not in visited
                    and grid[next_i][next_j] == 1
                ):
                    q.put((next_i, next_j, dist + 1))
                    visited.add((next_i, next_j))

        return -1

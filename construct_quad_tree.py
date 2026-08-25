# Definition for a QuadTree node.
from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs(n, r, c):
            allSame = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            if allSame:
                # NOTE: A leaf has been found.
                return Node(grid[r][c], True)

            n = n // 2
            topleft = dfs(n, r, c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r + n, c)
            bottomright = dfs(n, r + n, c + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid), 0, 0)

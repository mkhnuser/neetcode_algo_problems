from typing import List


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        visited = set()
        n = len(image)
        m = len(image[0])
        initial_color = image[sr][sc]
        self.recurse_dfs(image, sr, sc, color, visited, n, m, initial_color)
        return image

    def recurse_dfs(
        self,
        image: List[List[int]],
        i: int,
        j: int,
        color: int,
        visited: set[tuple[int, int]],
        n: int,
        m: int,
        initial_color: int,
    ) -> None:
        if (
            i < 0
            or i >= n
            or j < 0
            or j >= m
            or (i, j) in visited
            or image[i][j] != initial_color
        ):
            return

        visited.add((i, j))
        image[i][j] = color

        for dir in DIRECTIONS:
            i_incr, j_incr = dir
            self.recurse_dfs(
                image,
                i + i_incr,
                j + j_incr,
                color,
                visited,
                n,
                m,
                initial_color,
            )

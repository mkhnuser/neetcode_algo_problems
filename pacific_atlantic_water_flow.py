from queue import Queue
from typing import List


DIRECTIONS = (
    (-1, 0),  # top
    (0, -1),  # left
    (+1, 0),  # bottom
    (0, +1),  # right
)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # NOTE:
        # pacific = top, left.
        # atlantic = bottom, right.
        # Flow is allowed to the equal or lower cells.
        output = []

        if not heights:
            return output

        cells = self.bfs(heights, DIRECTIONS)
        output = [list(t) for t in cells]
        return output

    def bfs(
        self,
        heights: List[List[int]],
        directions: tuple[tuple[int, int], ...],
    ) -> set[tuple[int, int]]:
        set_: set[tuple[int, int]] = set()
        n = len(heights)
        m = len(heights[0])

        for init_i in range(n):
            for init_j in range(m):
                q = Queue()
                visited: set[tuple[int, int]] = set()

                q.put((init_i, init_j))
                visited.add((init_i, init_j))

                has_pacific_been_reached = False
                has_atlantic_been_reached = False

                while q.qsize() > 0:
                    i, j = q.get()

                    for dir in directions:
                        i_incr, j_incr = dir
                        next_i, next_j = i + i_incr, j + j_incr

                        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                            if next_i < 0 or next_j < 0:
                                has_pacific_been_reached = True
                            else:
                                has_atlantic_been_reached = True
                            continue

                        if (next_i, next_j) in visited or heights[next_i][
                            next_j
                        ] > heights[i][j]:
                            continue

                        q.put((next_i, next_j))
                        visited.add((next_i, next_j))

                if has_pacific_been_reached and has_atlantic_been_reached:
                    set_.add((init_i, init_j))

        return set_


def test() -> None:
    heights = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6],
    ]
    sol = Solution()
    print(sol.pacificAtlantic(heights))


if __name__ == "__main__":
    test()

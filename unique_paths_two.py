from typing import List


OK = 0
OBSTACLE = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # NOTE: 1 is an obstacle; 0 is a valid vertex.
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        return self.recurse_the_solution(obstacleGrid, n, m, 0, 0, n - 1, m - 1, {})

    def recurse_the_solution(
        self,
        obstacleGrid: list[list[int]],
        n: int,
        m: int,
        i: int,
        j: int,
        t1: int,
        t2: int,
        cache: dict,
    ) -> int:
        if i >= n or j >= m:
            return 0
        if obstacleGrid[i][j] == OBSTACLE:
            return 0

        if i == t1 and j == t2:
            return 1

        if (i, j) in cache:
            return cache[(i, j)]

        cache[(i, j)] = self.recurse_the_solution(
            obstacleGrid,
            n,
            m,
            i + 1,
            j,
            t1,
            t2,
            cache,
        ) + self.recurse_the_solution(
            obstacleGrid,
            n,
            m,
            i,
            j + 1,
            t1,
            t2,
            cache,
        )
        return cache[(i, j)]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # NOTE: 1 is an obstacle; 0 is a valid vertex.
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        return self.dp(obstacleGrid, n, m)

    def dp(self, obstacleGrid, n: int, m: int) -> int:
        prev_row = [0 for _ in range(m)]

        for r in range(n - 1, -1, -1):
            cur_row = [0 for _ in range(m)]

            for c in range(m - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    cur_row[c] = 0
                else:
                    if r == n - 1 and c == m - 1:
                        cur_row[c] = 1
                    elif c == m - 1:
                        cur_row[c] = prev_row[c]
                    else:
                        cur_row[c] = prev_row[c] + cur_row[c + 1]

            prev_row = cur_row

        return prev_row[0]


def test() -> None:
    obstacleGrid = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))

    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))


if __name__ == "__main__":
    test()

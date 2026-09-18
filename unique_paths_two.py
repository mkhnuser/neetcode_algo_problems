from typing import List, MutableMapping


DEAD_END_CELL = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = obstacleGrid
        n = len(matrix)
        m = len(matrix[0])
        return self.recurse(0, 0, n - 1, m - 1, matrix, n, m)

    def recurse(
        self,
        i: int,
        j: int,
        end_i: int,
        end_j: int,
        matrix: List[List[int]],
        n: int,
        m: int,
    ) -> int:
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0

        if matrix[i][j] == DEAD_END_CELL:
            return 0

        if i == end_i and j == end_j:
            return 1

        bottom_path = self.recurse(i + 1, j, end_i, end_j, matrix, n, m)
        right_path = self.recurse(i, j + 1, end_i, end_j, matrix, n, m)
        return bottom_path + right_path


from typing import List, MutableMapping

DEAD_END_CELL = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = obstacleGrid
        n = len(matrix)
        m = len(matrix[0])
        return self.recurse(0, 0, n - 1, m - 1, matrix, n, m, {})

    def recurse(
        self,
        i: int,
        j: int,
        end_i: int,
        end_j: int,
        matrix: List[List[int]],
        n: int,
        m: int,
        cache: MutableMapping[tuple[int, int], int],
    ) -> int:
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0

        if matrix[i][j] == DEAD_END_CELL:
            return 0

        if i == end_i and j == end_j:
            return 1

        if (i, j) in cache:
            return cache[(i, j)]

        bottom_path = self.recurse(i + 1, j, end_i, end_j, matrix, n, m, cache)
        right_path = self.recurse(i, j + 1, end_i, end_j, matrix, n, m, cache)
        cache[(i, j)] = bottom_path + right_path
        return cache[(i, j)]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = obstacleGrid
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] = "x"

        if matrix[n - 1][m - 1] == "x":
            return 0

        dp = [0 for _ in range(m)]
        dp[-1] = 1

        for j in range(m - 2, -1, -1):
            if matrix[-1][j] == "x":
                break
            dp[j] = 1

        for i in range(n - 2, -1, -1):
            current_dp_row = [0 for _ in range(m)]

            for j in range(m - 1, -1, -1):
                if matrix[i][j] == "x":
                    dp[j] = 0
                    continue

                if j == m - 1:
                    current_dp_row[j] = dp[j]
                else:
                    current_dp_row[j] = dp[j] + current_dp_row[j + 1]

            dp = current_dp_row

        return dp[0]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = obstacleGrid
        n = len(matrix)
        m = len(matrix[0])

        if matrix[n - 1][m - 1] == 1:
            return 0

        dp = [0 for _ in range(m)]
        dp[-1] = 1

        for j in range(m - 2, -1, -1):
            if matrix[-1][j] == 1:
                break
            dp[j] = 1

        for i in range(n - 2, -1, -1):
            current_dp_row = [0 for _ in range(m)]

            for j in range(m - 1, -1, -1):
                if matrix[i][j] == 1:
                    dp[j] = 0
                    continue

                if j == m - 1:
                    current_dp_row[j] = dp[j]
                else:
                    current_dp_row[j] = dp[j] + current_dp_row[j + 1]

            dp = current_dp_row

        return dp[0]


def test() -> None:
    obstacleGrid = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))

    obstacleGrid = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))

    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return self.recurse_the_solution(grid, n, m, 0, 0, {})

    def recurse_the_solution(
        self,
        grid: list[list[int]],
        n: int,
        m: int,
        i: int,
        j: int,
        cache: dict[tuple[int, int], int],
    ) -> int | float:
        if i >= n or j >= m:
            return float("+inf")
        if i == n - 1 and j == m - 1:
            return grid[i][j]

        if (i, j) in cache:
            return cache[(i, j)]

        bottom_path = (
            self.recurse_the_solution(grid, n, m, i + 1, j, cache) + grid[i][j]
        )
        right_path = self.recurse_the_solution(grid, n, m, i, j + 1, cache) + grid[i][j]
        min_path_summation = min(bottom_path, right_path)
        cache[(i, j)] = min_path_summation
        return cache[(i, j)]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return self.dp(grid, n, m)

    def dp(
        self,
        grid: list[list[int]],
        n: int,
        m: int,
    ) -> int:
        prev_row = [float("+inf") for _ in range(m)]

        for r in range(n - 1, -1, -1):
            cur_row = grid[r].copy()

            for c in range(m - 1, -1, -1):
                if r == n - 1 and c == m - 1:
                    # NOTE: The final vertex has been reached.
                    cur_row[c] = grid[r][c]
                elif c == m - 1:
                    cur_row[c] = cur_row[c] + prev_row[c]
                else:
                    cur_row[c] = min(
                        prev_row[c] + cur_row[c], cur_row[c + 1] + cur_row[c]
                    )

            prev_row = cur_row

        return prev_row[0]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return self.dp(grid, n, m)

    def dp(
        self,
        grid: list[list[int]],
        n: int,
        m: int,
    ) -> int:
        # NOTE: Create a gutter.
        dp = [float("+inf") for _ in range(m + 1)]
        dp[-2] = 0

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        return self.dp(grid, n, m)

    def dp(
        self,
        grid: list[list[int]],
        n: int,
        m: int,
    ) -> int:
        # NOTE: Create a gutter.
        dp = [[float("+inf") for _ in range(m + 1)] for __ in range(n + 1)]
        dp[n - 1][m] = 0

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]


def test() -> None:
    grid = [[1, 2, 0], [5, 4, 2], [1, 1, 3]]
    sol = Solution()
    print(sol.minPathSum(grid))

    grid = [[2, 2], [1, 0]]
    sol = Solution()
    print(sol.minPathSum(grid))


if __name__ == "__main__":
    test()

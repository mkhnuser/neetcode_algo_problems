from typing import MutableMapping


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        start_coords = (0, 0)
        end_coords = (m - 1, n - 1)
        return self.recurse(*start_coords, *end_coords, m, n)

    def recurse(
        self,
        i: int,
        j: int,
        end_i: int,
        end_j: int,
        m: int,
        n: int,
    ) -> int:
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0

        if i == end_i and j == end_j:
            return 1

        bottom_path = self.recurse(i + 1, j, end_i, end_j, m, n)
        right_path = self.recurse(i, j + 1, end_i, end_j, m, n)

        return bottom_path + right_path


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        start_coords = (0, 0)
        end_coords = (m - 1, n - 1)
        return self.recurse(*start_coords, *end_coords, m, n, {})

    def recurse(
        self,
        i: int,
        j: int,
        end_i: int,
        end_j: int,
        m: int,
        n: int,
        cache: MutableMapping[tuple[int, int], int],
    ) -> int:
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0

        if i == end_i and j == end_j:
            return 1

        if (i, j) in cache:
            return cache[(i, j)]

        bottom_path = self.recurse(i + 1, j, end_i, end_j, m, n, cache)
        right_path = self.recurse(i, j + 1, end_i, end_j, m, n, cache)
        cache[(i, j)] = bottom_path + right_path
        return cache[(i, j)]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for __ in range(m)]

        last_row = dp[m - 1]
        for i in range(n):
            last_row[i] = 1

        for i in range(m - 2, -1, -1):
            prev_dp_row = dp[i + 1]
            current_row = dp[i]

            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    current_row[j] = prev_dp_row[j]
                else:
                    current_row[j] = current_row[j + 1] + prev_dp_row[j]

        return dp[0][0]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(m - 2, -1, -1):
            current_row = [0] * n

            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    current_row[j] = dp[j]
                else:
                    current_row[j] = current_row[j + 1] + dp[j]

            dp = current_row

        return dp[0]


def test() -> None:
    sol = Solution()
    print(sol.uniquePaths(3, 6))


if __name__ == "__main__":
    test()

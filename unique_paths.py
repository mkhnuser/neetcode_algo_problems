class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # NOTE: m = the number of rows; n = cols.
        return self.recurse_the_solution(m, n, 0, 0, m - 1, n - 1, {})

    def recurse_the_solution(
        self,
        m: int,
        n: int,
        i: int,
        j: int,
        t1: int,
        t2: int,
        cache: dict,
    ) -> int:
        if i >= m or j >= n:
            return 0
        if i == t1 and j == t2:
            return 1

        if (i, j) in cache:
            return cache[(i, j)]

        cache[(i, j)] = self.recurse_the_solution(
            m,
            n,
            i + 1,
            j,
            t1,
            t2,
            cache,
        ) + self.recurse_the_solution(
            m,
            n,
            i,
            j + 1,
            t1,
            t2,
            cache,
        )
        return cache[(i, j)]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # NOTE: m = the number of rows; n = cols.
        return self.dp(m, n)

    def dp(self, m: int, n: int) -> int:
        prev_row = [0 for _ in range(n)]
        for r in range(m - 1, -1, -1):
            cur_row = [0 for _ in range(n)]
            cur_row[-1] = 1
            for c in range(n - 2, -1, -1):
                cur_row[c] = cur_row[c + 1] + prev_row[c]
            prev_row = cur_row
        return prev_row[0]


def test() -> None:
    m = 3
    n = 6
    sol = Solution()
    print(sol.uniquePaths(m, n))

    m = 3
    n = 3
    sol = Solution()
    print(sol.uniquePaths(m, n))


if __name__ == "__main__":
    test()

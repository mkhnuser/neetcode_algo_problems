from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        i = 0
        n = len(profit)
        cache = [[-1 for __ in range(capacity + 1)] for _ in range(n)]
        return self.recurse(profit, weight, n, i, cache, capacity)

    def recurse(
        self,
        profit: list[int],
        weight: list[int],
        n: int,
        i: int,
        cache: list[list[int]],
        available_space: int,
    ) -> int:
        # NOTE: What's the max profit which can be obtained from items 0..i inclusively, given capacity `availabe_space`?

        if i >= n:
            return 0

        if cache[i][available_space] != -1:
            return cache[i][available_space]

        p = profit[i]
        w = weight[i]

        inclusion_path = 0
        if available_space - w >= 0:
            inclusion_path = p + self.recurse(
                profit, weight, n, i + 1, cache, available_space - w
            )

        exclusion_path = self.recurse(profit, weight, n, i + 1, cache, available_space)
        cache[i][available_space] = max(inclusion_path, exclusion_path)
        return cache[i][available_space]


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity

        # NOTE: Let dp[i][j] answer the question:
        # Given items 0..i inclusively, what's the max profit which can be obtained, given capacity j?
        dp = [[0 for _ in range(M + 1)] for __ in range(N)]

        # NOTE: It's impossible to have any profit if your available space is zero.
        for i in range(N):
            dp[i][0] = 0

        for j in range(M + 1):
            if weight[0] <= j:
                dp[0][j] = profit[0]

        for i in range(1, N):
            for j in range(M + 1):
                inclusion_path = 0
                if j - weight[i] >= 0:
                    inclusion_path = profit[i] + dp[i - 1][j - weight[i]]

                exclusion_path = dp[i - 1][j]
                dp[i][j] = max(inclusion_path, exclusion_path)

        return dp[N - 1][M]


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity

        # NOTE: Let dp[i][j] answer the question:
        # Given items 0..i inclusively, what's the max profit which can be obtained, given capacity j?
        dp = [0 for _ in range(M + 1)]

        for j in range(M + 1):
            if weight[0] <= j:
                dp[j] = profit[0]

        for i in range(1, N):
            current_dp_row = [0 for _ in range(M + 1)]

            for j in range(M + 1):
                inclusion_path = 0
                if j - weight[i] >= 0:
                    inclusion_path = profit[i] + dp[j - weight[i]]

                exclusion_path = dp[j]
                current_dp_row[j] = max(inclusion_path, exclusion_path)

            dp = current_dp_row

        return dp[M]


def test() -> None:
    profit = [4, 4, 7, 1]
    weight = [5, 2, 3, 1]
    capacity = 8

    sol = Solution()
    print(sol.maximumProfit(profit, weight, capacity))


if __name__ == "__main__":
    test()

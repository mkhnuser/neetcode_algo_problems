from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        i = 0
        n = len(profit)
        cache = [[-1 for _ in range(capacity + 1)] for __ in range(n)]
        return self.recurse(profit, weight, n, cache, i, capacity)

    def recurse(
        self,
        profit: list[int],
        weight: list[int],
        n: int,
        cache: list[list[int]],
        i: int,
        capacity: int,
    ) -> int:
        if i >= n:
            return 0

        if cache[i][capacity] != -1:
            return cache[i][capacity]

        w = weight[i]
        p = profit[i]

        inclusion_path = 0

        if capacity - w >= 0:
            inclusion_path = p + self.recurse(profit, weight, n, cache, i, capacity - w)

        exclusion_path = self.recurse(profit, weight, n, cache, i + 1, capacity)
        cache[i][capacity] = max(inclusion_path, exclusion_path)
        return cache[i][capacity]


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity

        # NOTE: dp[i][j] answers a question:
        # Given items 0..i, and a capacity j, what's the max profit?
        dp = [[0 for _ in range(M + 1)] for __ in range(N)]

        for i in range(N):
            dp[i][0] = 0

        for j in range(M + 1):
            if weight[0] <= j:
                dp[0][j] = (j // weight[0]) * profit[0]

        for i in range(1, N):
            for j in range(M + 1):
                inclusion_path = 0

                if j - weight[i] >= 0:
                    inclusion_path = profit[i] + dp[i][j - weight[i]]

                exclusion_path = dp[i - 1][j]
                dp[i][j] = max(inclusion_path, exclusion_path)

        return dp[N - 1][M]


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity

        # NOTE: dp[i][j] answers a question:
        # Given items 0..i, and a capacity j, what's the max profit?
        dp = [0 for _ in range(M + 1)]

        for j in range(M + 1):
            if weight[0] <= j:
                dp[j] = (j // weight[0]) * profit[0]

        for i in range(1, N):
            current_dp_row = [0 for _ in range(M + 1)]

            for j in range(M + 1):
                inclusion_path = 0

                if j - weight[i] >= 0:
                    inclusion_path = profit[i] + current_dp_row[j - weight[i]]

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

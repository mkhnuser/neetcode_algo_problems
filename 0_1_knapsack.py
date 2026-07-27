from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # NOTE: Total weight should be <= capacity.
        n = len(profit)
        return self.recurse(profit, weight, capacity, n, 0, 0, 0)

    def recurse(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
        n: int,
        i: int,
        profit_so_far: int,
        weight_so_far: int,
    ) -> int:
        if i >= n:
            return profit_so_far

        current_profit = profit[i]
        current_weight = weight[i]

        if weight_so_far + current_weight > capacity:
            # NOTE: Definitely not include the current item since it exceeds the capacity.
            return self.recurse(
                profit,
                weight,
                capacity,
                n,
                i + 1,
                profit_so_far,
                weight_so_far,
            )

        return max(
            self.recurse(
                profit,
                weight,
                capacity,
                n,
                i + 1,
                profit_so_far + current_profit,
                weight_so_far + current_weight,
            ),
            self.recurse(
                profit,
                weight,
                capacity,
                n,
                i + 1,
                profit_so_far,
                weight_so_far,
            ),
        )


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # NOTE: Total weight should be <= capacity.
        n = len(profit)
        return self.recurse(profit, weight, capacity, n, 0)

    def recurse(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
        n: int,
        i: int,
    ) -> int:
        if i >= n:
            return 0

        # NOTE: Include.
        capacity -= weight[i]
        included = 0

        if capacity >= 0:
            included = profit[i] + self.recurse(profit, weight, capacity, n, i + 1)

        # NOTE: Exclude.
        capacity += weight[i]
        excluded = self.recurse(profit, weight, capacity, n, i + 1)
        return max(included, excluded)


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # NOTE: Total weight should be <= capacity.
        return self.dp(profit, weight, capacity)

    def dp(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
    ) -> int:
        N = len(profit)
        M = capacity
        dp = [[0 for _ in range(M + 1)] for __ in range(N)]
        # NOTE: The question dp[i][j] answers is as follows:
        # Given capacity j, what's the maximum profit that can be obtained from profit[0:i + 1]?
        for i in range(N):
            dp[i][0] = 0

        for j in range(M + 1):
            dp[0][j] = 0 if weight[0] > j else profit[0]

        for i in range(1, N):
            for j in range(1, M + 1):
                excluded = dp[i - 1][j]

                included = 0
                # NOTE: Can we even include the current item?
                if j - weight[i] >= 0:
                    included = profit[i] + dp[i - 1][j - weight[i]]

                dp[i][j] = max(excluded, included)

        return dp[N - 1][M]


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # NOTE: Total weight should be <= capacity.
        return self.dp(profit, weight, capacity)

    def dp(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
    ) -> int:
        N = len(profit)
        M = capacity
        dp = [0 for _ in range(M + 1)]
        # NOTE: The question dp[i][j] answers is as follows:
        # Given capacity j, what's the maximum profit that can be obtained from profit[0:i + 1]?
        for j in range(1, len(dp)):
            dp[j] = 0 if weight[0] > j else profit[0]

        for i in range(1, N):
            current_row = [0 for _ in range(M + 1)]
            for j in range(1, M + 1):
                excluded = dp[j]
                included = 0
                if j - weight[i] >= 0:
                    included = profit[i] + dp[j - weight[i]]
                current_row[j] = max(included, excluded)
            dp = current_row

        return dp[-1]


def test() -> None:
    # NOTE:   0  1  2  3.
    profit = [4, 4, 7, 1]
    weight = [5, 2, 3, 1]
    capacity = 8
    sol = Solution()
    print(sol.maximumProfit(profit, weight, capacity))

    profit = [1, 2, 3]
    weight = [4, 5, 1]
    capacity = 4
    sol = Solution()
    print(sol.maximumProfit(profit, weight, capacity))


if __name__ == "__main__":
    test()

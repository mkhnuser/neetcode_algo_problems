from typing import List


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.recurse(profit, weight, capacity, 0)

    def recurse(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
        i: int,
    ) -> int:
        if i >= len(profit):
            return 0

        # NOTE: Let's skip the current item first.
        exclusive_path = self.recurse(profit, weight, capacity, i + 1)

        # NOTE: Let's try to include the current item now.
        inclusive_path = 0
        new_capacity = capacity - weight[i]
        if new_capacity >= 0:
            inclusive_path = profit[i] + self.recurse(profit, weight, new_capacity, i)

        return max(exclusive_path, inclusive_path)


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.recurse(profit, weight, capacity, 0, {})

    def recurse(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
        i: int,
        cache: dict,
    ) -> int:
        if i >= len(profit):
            return 0

        if (i, capacity) in cache:
            return cache[(i, capacity)]

        # NOTE: Let's skip the current item first.
        exclusive_path = self.recurse(profit, weight, capacity, i + 1, cache)

        # NOTE: Let's try to include the current item now, which can be chosen multiple times.
        inclusive_path = 0
        new_capacity = capacity - weight[i]
        if new_capacity >= 0:
            inclusive_path = profit[i] + self.recurse(
                profit,
                weight,
                new_capacity,
                i,
                cache,
            )

        cache[(i, capacity)] = max(exclusive_path, inclusive_path)
        return cache[(i, capacity)]


class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
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

        for c in range(M + 1):
            dp[0][c] = profit[0] if weight[0] <= c else 0

        for i in range(N):
            dp[i][0] = 0

        for i in range(N):
            for j in range(M + 1):
                exclusive_path = dp[i - 1][j]

                inclusive_path = 0
                new_capacity = j - weight[i]

                if new_capacity >= 0:
                    inclusive_path = profit[i] + dp[i][new_capacity]

                dp[i][j] = max(exclusive_path, inclusive_path)

        return dp[N - 1][M]


def test() -> None:
    profit = [4, 4, 7, 1]
    weight = [5, 2, 3, 1]
    capacity = 8
    sol = Solution()
    print(sol.maximumProfit(profit, weight, capacity))


if __name__ == "__main__":
    test()

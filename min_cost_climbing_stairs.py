from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dfs(index: int) -> int:
            if index >= n:
                return 0

            if index in memo:
                return memo[index]

            c1 = dfs(index + 1)
            c2 = dfs(index + 2)
            min_cost = min(c1, c2) + cost[index]
            memo[index] = min_cost
            return min_cost

        # NOTE: Let's explore all possible jumps from i = 0 and i = 1 and return a path with min cost.
        return min(dfs(0), dfs(1))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # NOTE:
        # The cost has been paid, just +1 or +2.
        # You can start at i = 0 or i = 1.
        # The question we pose is: given an index i, what's the min cost to reach i?

        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])


def test() -> None:
    cost = [1, 2, 3]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))

    cost = [1, 2, 1, 2, 1, 1, 1]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))


if __name__ == "__main__":
    test()

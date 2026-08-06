import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        res = self.recurse(coins, amount, 0, 0, 0, {})

        if math.isinf(res):
            return -1

        return res

    def recurse(
        self,
        coins: List[int],
        amount: int,
        i: int,
        summation: int,
        depth: int,
        cache: dict,
    ) -> int:
        # NOTE: Find the fewest number of coins such that their sum equals amount.
        if i >= len(coins):
            return float("+inf")
        if summation == amount:
            return depth
        if summation > amount:
            return float("+inf")

        if (i, summation, depth) in cache:
            return cache[(i, summation, depth)]

        # NOTE: Exclude the current coin.
        exclusion_path = self.recurse(coins, amount, i + 1, summation, depth, cache)
        # NOTE: Include the current coin.
        coin_amount = coins[i]
        inclusion_path = self.recurse(
            coins,
            amount,
            i,
            summation + coin_amount,
            depth + 1,
            cache,
        )
        cache[(i, summation, depth)] = min(exclusion_path, inclusion_path)
        return cache[(i, summation, depth)]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [(float("+inf")) for _ in range(amount + 1)]
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float("+inf") else -1


def test() -> None:
    coins = [1, 5, 10]
    amount = 12
    sol = Solution()
    print(sol.coinChange(coins, amount))

    coins = [2]
    amount = 3
    sol = Solution()
    print(sol.coinChange(coins, amount))

    coins = [1]
    amount = 0
    sol = Solution()
    print(sol.coinChange(coins, amount))

    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))


if __name__ == "__main__":
    test()

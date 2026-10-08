from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # NOTE: Let dp[a] answer the question: "How many coins does one need, so that the amount of a is obtained?"
        dp = [float("+inf") for _ in range(amount + 1)]
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if not math.isinf(dp[amount]) else -1

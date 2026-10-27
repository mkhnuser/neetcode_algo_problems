from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[None] * 2 for _ in range(n)]

        def dfs(i, alice):
            if i >= n:
                return 0
            if dp[i][alice] is not None:
                return dp[i][alice]

            res = float("-inf") if alice == 1 else float("inf")
            score = 0
            for j in range(i, min(i + 3, n)):
                if alice == 1:
                    score += stoneValue[j]
                    res = max(res, score + dfs(j + 1, 0))
                else:
                    score -= stoneValue[j]
                    res = min(res, score + dfs(j + 1, 1))

            dp[i][alice] = res
            return res

        result = dfs(0, 1)
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"

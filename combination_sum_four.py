from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # NOTE: dp[t] answers a question, given a target `t`, how many ways are there to obtain it?
        dp = [-1 for _ in range(target + 1)]
        # NOTE: There is only one way to reach the target of zero.
        dp[0] = 1

        for t in range(1, target + 1):
            dp[t] = 0

            for n in nums:
                if t - n >= 0:
                    dp[t] += dp[t - n]

        return dp[target]

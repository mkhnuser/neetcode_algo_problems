from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("+inf") for _ in range(n)]
        # NOTE: dp[i] <=> the min number of jumps from `i` to `n - 1`.
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            max_jump_length = nums[i]

            for j in range(i + 1, i + max_jump_length + 1):
                if j >= n:
                    break
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]

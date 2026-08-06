from typing import List
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(i: int, current_summation: int, cache: dict) -> int:
            if i >= n:
                if current_summation == target:
                    return 1
                if current_summation < target or current_summation > target:
                    return 0

            if (i, current_summation) in cache:
                return cache[(i, current_summation)]

            positive_path = dfs(i + 1, current_summation + nums[i], {})
            negative_path = dfs(i + 1, current_summation - nums[i], {})
            cache[(i, current_summation)] = positive_path + negative_path
            return cache[(i, current_summation)]

        return dfs(0, 0, {})


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        # NOTE: dp[i][key] returns 0 by default now.
        # dp[i][cur_sum] = count <=> how many ways are there to form <cur_sum> using up to <nums[:i]> numbers?
        dp[0][0] = 1

        for i in range(n):
            for summation, count in dp[i].items():
                dp[i + 1][summation + nums[i]] += count
                dp[i + 1][summation - nums[i]] += count

        # NOTE: Given the sum <target>, how many ways are there to reach it using <n> numbers?
        return dp[n][target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n):
            current_dp = defaultdict(int)
            for summation, count in dp.items():
                current_dp[summation + nums[i]] += count
                current_dp[summation - nums[i]] += count
            dp = current_dp

        return dp[target]


def test() -> None:
    sol = Solution()
    print(sol.findTargetSumWays([2, 2, 2], 2))


if __name__ == "__main__":
    test()

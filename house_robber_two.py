from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return max(nums)

        # NOTE: Separate into two cases:
        # 1. Allow the first house but exclude the last one.
        # 2. Exclude the last house but allow the first one.

        output1 = self.dp_solution(nums[:-1], n - 1)
        output2 = self.dp_solution(nums[1:], n - 1)
        return max(output1, output2)

    def dp_solution(self, nums: List[int], n: int) -> int:
        if not nums:
            return 0
        if n == 1:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for j in range(2, n):
            dp[j] = max(dp[j - 1], dp[j - 2] + nums[j])

        return dp[-1]


def test() -> None:
    nums = [3, 4, 3]
    sol = Solution()
    print(sol.rob(nums))

    nums = [2, 9, 8, 3, 6]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    test()

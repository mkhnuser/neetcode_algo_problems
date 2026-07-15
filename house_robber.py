from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: Given an index i, what's the max profit you can achieve?
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: Given an index i, what's the max profit you can achieve?
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return max(nums)

        p1 = nums[0]
        p2 = max(nums[0], nums[1])
        j = 2

        while j < n:
            p1, p2 = p2, max(p2, p1 + nums[j])
            j += 1

        return p2


def test() -> None:
    nums = [1, 1, 3, 3]
    sol = Solution()
    print(sol.rob(nums))

    nums = [2, 9, 8, 3, 6]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    test()

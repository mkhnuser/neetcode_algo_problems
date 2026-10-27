from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        return self.recurse(nums, dp, 1, len(nums) - 2)

    def recurse(self, nums: list[int], dp: dict, L: int, R: int) -> int:
        if L > R:
            return 0
        if (L, R) in dp:
            return dp[(L, R)]

        dp[(L, R)] = 0

        for i in range(L, R + 1):
            coins = nums[L - 1] * nums[i] * nums[R + 1]
            coins += self.recurse(nums, dp, L, i - 1) + self.recurse(nums, dp, i + 1, R)
            dp[(L, R)] = max(dp[(L, R)], coins)

        return dp[(L, R)]


def test() -> None:
    nums = [4, 2, 3, 7]
    sol = Solution()
    print(sol.maxCoins(nums))


if __name__ == "__main__":
    test()

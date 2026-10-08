from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1 for _ in range(n)]
        return max(self.recurse(nums, n, cache, i) for i in range(n))

    def recurse(self, nums: List[int], n: int, cache: list[int], i: int) -> int:
        if i >= n:
            return 0

        if cache[i] != -1:
            return cache[i]

        # NOTE: Starting from index `i`, what's the length of LIS?
        LIS = 1

        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                LIS = max(LIS, 1 + self.recurse(nums, n, cache, j))

        cache[i] = LIS
        return cache[i]


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


def test() -> None:
    sol = Solution()
    print(sol.lengthOfLIS(nums=[9, 1, 4, 2, 3, 3, 7]))

    sol = Solution()
    print(sol.lengthOfLIS(nums=[0, 3, 1, 3, 2, 3]))

    sol = Solution()
    print(sol.lengthOfLIS(nums=[4, 10, 4, 3, 8, 9]))


if __name__ == "__main__":
    test()

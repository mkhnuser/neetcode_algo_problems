from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)

        if summation % 2 != 0:
            return False

        half_summation = summation // 2
        i = 0
        n = len(nums)
        first_subset_summation = 0
        # NOTE: sum_1 + sum_2 == 2 * sum_1 == summation <=> sum_1 == half_summation.
        return self.recurse(nums, n, half_summation, i, first_subset_summation, {})

    def recurse(
        self,
        nums: List[int],
        n: int,
        half_summation: int,
        i: int,
        first_subset_summation: int,
        cache: dict,
    ) -> bool:
        if i >= n:
            return first_subset_summation == half_summation

        if (i, first_subset_summation) in cache:
            return cache[(i, first_subset_summation)]

        first_subset_summation += nums[i]
        inclusion_path = self.recurse(
            nums,
            n,
            half_summation,
            i + 1,
            first_subset_summation,
            cache,
        )
        if inclusion_path:
            return True

        first_subset_summation -= nums[i]
        exclusion_path = self.recurse(
            nums,
            n,
            half_summation,
            i + 1,
            first_subset_summation,
            cache,
        )
        if exclusion_path:
            return True

        cache[(i, first_subset_summation)] = False
        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)

        if summation % 2 != 0:
            return False

        half_summation = summation // 2

        set_ = {0}

        for i in range(len(nums) - 1, -1, -1):
            stage = set_.copy()
            num = nums[i]

            for s in set_:
                stage.add(s + num)

            if half_summation in stage:
                return True

            set_ = stage

        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 != 0:
            return False

        n = len(nums)
        half_summation = summation // 2

        # NOTE: dp[i][j] answers a question:
        # Given numbers nums[:i + 1], is it possible to reach the target j?
        dp = [[False] * (half_summation + 1) for _ in range(n + 1)]

        # NOTE: Given any number of items, it's always possible to reach the target of zero, just choose nothing.
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, half_summation + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][half_summation]


def test() -> None:
    sol = Solution()
    print(sol.canPartition(nums=[1, 2, 3, 4]))
    sol = Solution()
    print(sol.canPartition(nums=[1, 2, 3, 4, 5]))


if __name__ == "__main__":
    test()

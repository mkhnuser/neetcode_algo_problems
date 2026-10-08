from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        cache = {}
        return self.recurse(nums, n, i, target, cache)

    def recurse(
        self,
        nums: List[int],
        n,
        i: int,
        target: int,
        cache: dict,
    ) -> int:
        if i >= n:
            if target == 0:
                return 1
            else:
                return 0

        if (i, target) in cache:
            return cache[(i, target)]

        plus_path = self.recurse(
            nums,
            n,
            i + 1,
            target + nums[i],
            cache,
        )
        minus_path = self.recurse(
            nums,
            n,
            i + 1,
            target - nums[i],
            cache,
        )
        cache[(i, target)] = plus_path + minus_path
        return cache[(i, target)]

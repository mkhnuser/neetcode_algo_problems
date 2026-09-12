from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)

        if total_sum % k != 0:
            return False

        max_subset_sum = total_sum // k
        sums = [0] * k
        return self.recurse(nums, 0, sums, max_subset_sum, k)

    def recurse(
        self,
        nums: List[int],
        i: int,
        sums: list[int],
        max_subset_sum: int,
        k: int,
    ) -> bool:
        if i >= len(nums):
            summation = sums[0]
            for s in sums:
                if s != summation:
                    return False
            return True

        for j in range(k):
            if sums[j] + nums[i] <= max_subset_sum:
                sums[j] += nums[i]

                if self.recurse(nums, i + 1, sums, max_subset_sum, k):
                    return True

                sums[j] -= nums[i]

        return False


def test() -> None:
    nums = [2, 4, 1, 3, 5]
    k = 3
    sol = Solution()
    print(sol.canPartitionKSubsets(nums, k))

    nums = [1, 2, 3, 4]
    k = 3
    sol = Solution()
    print(sol.canPartitionKSubsets(nums, k))


if __name__ == "__main__":
    test()

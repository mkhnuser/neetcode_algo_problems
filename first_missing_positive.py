class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            abs_val = abs(nums[i])

            if 1 <= abs_val <= len(nums):
                if nums[abs_val - 1] > 0:
                    nums[abs_val - 1] *= -1
                elif nums[abs_val - 1] == 0:
                    nums[abs_val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            # NOTE: Assume that if nums[i - 1] is negative, then <i> exists in the array.
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1

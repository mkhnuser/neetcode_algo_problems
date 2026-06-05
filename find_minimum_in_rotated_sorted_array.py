from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1
        min_ = nums[0]

        while lower_bound <= upper_bound:
            if nums[lower_bound] <= nums[upper_bound]:
                min_ = min(min_, nums[lower_bound])
                break

            middle_index = (lower_bound + upper_bound) // 2
            cur = nums[middle_index]
            min_ = min(cur, min_)

            if cur >= nums[lower_bound]:
                lower_bound = middle_index + 1
            else:
                upper_bound = middle_index - 1

        return min_

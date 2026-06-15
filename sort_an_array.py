import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.recurse_sorting(nums)

    def recurse_sorting(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if len(nums) == 1:
            return nums

        pivot = random.choice(nums)
        less_than = [num for num in nums if num < pivot]
        equal_to = [num for num in nums if num == pivot]
        greater_than_or_equal_to = [num for num in nums if num > pivot]
        return (
            self.recurse_sorting(less_than)
            + equal_to
            + self.recurse_sorting(greater_than_or_equal_to)
        )

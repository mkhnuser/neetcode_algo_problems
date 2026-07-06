import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minimum_size = float("+inf")
        current_summation = 0

        for R in range(0, len(nums)):
            current_summation += nums[R]

            while current_summation >= target:
                minimum_size = min(minimum_size, R - L + 1)
                current_summation -= nums[L]
                L += 1

        return int(minimum_size) if not math.isinf(minimum_size) else 0

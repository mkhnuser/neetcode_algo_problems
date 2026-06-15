from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {}

        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1

        majority_threshhold = len(nums) // 2

        for num, counter in mapping.items():
            if counter >= majority_threshhold:
                return num

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


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]

        for el in nums:
            if el == major:
                count += 1
            else:
                count -= 1

            if count == 0:
                major = el
                count = 1

        # NOTE: Note the a majority element might not be present.
        c = 0
        for el in nums:
            if el == major:
                c += 1

        majority_threshhold = len(nums) // 2

        if c <= majority_threshhold:
            raise RuntimeError("No major was actually found!")

        return major

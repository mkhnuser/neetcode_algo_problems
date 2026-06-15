from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num_to_counter_mapping = [0 for _ in range(3)]
        for num in nums:
            num_to_counter_mapping[num] += 1

        j = 0
        for num in range(3):
            while num_to_counter_mapping[num]:
                nums[j] = num
                num_to_counter_mapping[num] -= 1
                j += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        L, R = 0, len(nums) - 1
        i = 0

        while i <= R:
            if nums[i] == 0:
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
            elif nums[i] == 2:
                nums[i], nums[R] = nums[R], nums[i]
                R -= 1
                i -= 1
            i += 1

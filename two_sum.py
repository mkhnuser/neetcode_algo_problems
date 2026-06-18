from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # NOTE: Let's map nums to indecies.
        mapping = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in mapping:
                return [mapping[diff], i]

            mapping[num] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = nums.copy()
        # NOTE: Just preserve the original indecies.
        A = [(num, i) for i, num in enumerate(A)]
        A.sort()

        i = 0
        j = len(A) - 1
        while i < j:
            current_sum = A[i][0] + A[j][0]
            if current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1
            else:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        index = 0
        current_subset = []
        self.backtrack(index, current_subset, nums, output)
        return output

    def backtrack(
        self,
        index: int,
        current_subset: List[int],
        nums: List[int],
        output: List[List[int]],
    ) -> None:
        if index >= len(nums):
            output.append(current_subset.copy())
            return

        current_subset.append(nums[index])
        self.backtrack(index + 1, current_subset, nums, output)
        current_subset.pop()

        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1

        self.backtrack(index + 1, current_subset, nums, output)

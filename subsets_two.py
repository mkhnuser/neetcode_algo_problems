from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        index = 0
        current_subset = []

        self.solve_with_backtracking(index, nums, output, current_subset)

        return output

    def solve_with_backtracking(
        self,
        index: int,
        nums: List[int],
        output: List[List[int]],
        current_subset: List[int],
    ) -> None:
        if index >= len(nums):
            output.append(current_subset.copy())
            return

        current_subset.append(nums[index])
        self.solve_with_backtracking(index + 1, nums, output, current_subset)
        current_subset.pop()

        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1

        self.solve_with_backtracking(index + 1, nums, output, current_subset)

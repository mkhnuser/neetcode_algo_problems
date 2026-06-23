from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # index = 0
        # current_subset = []
        # output = []
        # self.backtrack(index, current_subset, nums, output)
        # return output
        return self.iterate(nums)

    def iterate(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            new_output = []
            for s in output:
                new_s = s.copy()
                new_s.append(num)
                new_output.append(new_s)
            output += new_output
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
        self.backtrack(index + 1, current_subset, nums, output)

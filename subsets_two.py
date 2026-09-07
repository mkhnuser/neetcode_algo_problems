from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        self.gen(nums, [], 0, output)
        return output

    def gen(
        self,
        nums: List[int],
        s: List[int],
        p: int,
        output: List[List[int]],
    ) -> None:
        if p >= len(nums):
            output.append(s.copy())
            return None

        # NOTE: Include the current num.
        s.append(nums[p])
        self.gen(nums, s, p + 1, output)

        s.pop()

        # NOTE: Exclude every occurrence of the current num.
        t = p
        while t < len(nums) and nums[t] == nums[p]:
            t += 1

        self.gen(nums, s, t, output)

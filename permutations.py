from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        self.recurse(nums, output, [], n)
        return output

    def recurse(
        self,
        nums: List[int],
        output: List[List[int]],
        current_perm: List[int],
        n: int,
    ) -> None:
        for i in range(len(nums)):
            c = nums[i]
            new_nums = nums[:i] + nums[i + 1 :]
            current_perm.append(c)
            self.recurse(new_nums, output, current_perm, n)
            current_perm.pop()

        if len(current_perm) == n:
            output.append(current_perm.copy())

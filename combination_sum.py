from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        self.gen(0, 0, [], nums, target, output)
        return output

    def gen(
        self,
        p: int,
        s: int,
        c: List[int],
        nums: List[int],
        target: int,
        output: List[List[int]],
    ) -> None:
        if s == target:
            output.append(c.copy())
            return None

        if s > target:
            return None

        for i in range(p, len(nums)):
            num = nums[i]

            c.append(num)
            self.gen(i, s + num, c, nums, target, output)
            c.pop()

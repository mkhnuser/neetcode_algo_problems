from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for n in nums:
            stage = []

            for s in output:
                new_s = s.copy()
                new_s.append(n)
                stage.append(new_s)

            output.extend(stage)

        return output


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # NOTE: nums = [1] => [[1], []].
        # NOTE: nums = [1, 2] => [[1, 2], [1], [2], []].
        subsets = []
        self.gen(nums, subsets, [], 0)
        return subsets

    def gen(
        self,
        nums: List[int],
        subsets: List[List[int]],
        s: List[int],
        p: int,
    ) -> None:
        if p >= len(nums):
            subsets.append(s.copy())
            return None

        el = nums[p]
        s.append(el)
        self.gen(nums, subsets, s, p + 1)
        s.pop()
        self.gen(nums, subsets, s, p + 1)

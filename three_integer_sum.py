from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # NOTE:
        # 1. Return nums, not i, j, k.
        # 2. At the same time, i != j and j != k and i != k.
        # 3. target = 0.

        output = set()
        event_horizon = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                summation = nums[i] + nums[j]

                if -summation in event_horizon:
                    list_repr = [-summation, nums[i], nums[j]]
                    list_repr.sort()
                    tuple_repr = tuple(list_repr)
                    output.add(tuple_repr)

            event_horizon.add(nums[i])

        return [list(o) for o in output]

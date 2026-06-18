from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # NOTE:
        # 1. Return nums, not indecies.
        # 2. All indecies have to be distinct.
        # 3. target is given.

        output = set()
        event_horizon = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    diff = target - (nums[i] + nums[j] + nums[k])
                    # NOTE: target = diff + (nums[i] + nums[j] + nums[k]).
                    # So let's check whether diff can be found in our event horizon.

                    if diff in event_horizon:
                        list_repr = [diff, nums[i], nums[j], nums[k]]
                        list_repr.sort()
                        tuple_repr = tuple(list_repr)
                        output.add(tuple_repr)

            event_horizon.add(nums[i])

        return [list(o) for o in output]

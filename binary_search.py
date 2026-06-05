from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle_index = (L + R) // 2
            current = nums[middle_index]
            if current == target:
                return middle_index
            elif current > target:
                R = middle_index - 1
            else:
                L = middle_index + 1

        return -1

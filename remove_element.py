from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        counter = 0

        for i in range(n):
            current_val = nums[i]
            if current_val == val:
                nums[i] = float("+inf")
                counter += 1

        nums.sort()
        return n - counter

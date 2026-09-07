from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        range_ = range(0, n)

        for candidate in range_:
            xor ^= candidate ^ nums[candidate]

        return xor


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        output = n

        for p in range(0, n):
            output += p
            output -= nums[p]

        return output

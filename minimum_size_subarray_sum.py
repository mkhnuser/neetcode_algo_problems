import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = float("+inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                summation = sum(nums[i : j + 1])
                if summation >= target:
                    arr_size = (j - i) + 1
                    if arr_size < output:
                        output = arr_size
        return output if not math.isinf(output) else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = float("+inf")
        L = 0
        summation = 0

        for R in range(len(nums)):
            summation += nums[R]

            while summation >= target:
                output = min(((R - L) + 1), output)
                summation -= nums[L]
                L += 1

        return output if not math.isinf(output) else 0


def test():
    target = 10
    nums = [2, 1, 5, 1, 5, 3]
    #       0  1  2  3  4  5.
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))

    target = 5
    nums = [1, 2, 1]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))

    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    print(sol.minSubArrayLen(target, nums))


if __name__ == "__main__":
    test()

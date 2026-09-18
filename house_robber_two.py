from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: A B C. => check: A B or B C.
        # NOTE: A B C D. => check: A B C or B C D.
        # etc...
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(
            self.calculate(nums, 1, len(nums) - 1),
            self.calculate(nums, 0, len(nums) - 2),
        )

    def calculate(self, nums: List[int], L: int, R: int) -> int:
        # NOTE:
        # a = max profit up until the prev house inclusively.
        # b = max profit up until the current house inclusively.
        a = nums[L]
        b = max(nums[L], nums[L + 1])

        for i in range(L + 2, R + 1):
            a, b = b, max(nums[i] + a, b)

        return b


def test() -> None:
    nums = [3, 4, 3]
    sol = Solution()
    print(sol.rob(nums))

    nums = [2, 9, 8, 3, 6]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    test()

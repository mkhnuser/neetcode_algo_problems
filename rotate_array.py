from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], L: int, R: int) -> None:
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        for _ in range(k):
            self.shift_right(nums)

    def shift_right(self, nums: List[int]) -> None:
        last = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last

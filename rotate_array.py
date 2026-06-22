from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # for _ in range(k):
        #     self.shift_by_one_position_to_the_right(nums)
        n = len(nums)
        k %= n
        self.reverse_in_place(0, n - 1, nums)
        self.reverse_in_place(0, k - 1, nums)
        self.reverse_in_place(k, n - 1, nums)

    def reverse_in_place(self, start: int, end: int, nums: List[int]) -> None:
        # NOTE: Start and end are inclusive.
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def shift_by_one_position_to_the_right(self, nums: List[int]) -> None:
        last = nums[-1]

        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i - 1]

        nums[0] = last

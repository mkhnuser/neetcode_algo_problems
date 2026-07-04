from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        output = float("+inf")

        while L <= R:
            middle_index = (L + R) // 2
            middle_value = nums[middle_index]
            leftmost_value = nums[L]
            rightmost_value = nums[R]
            output = min(output, middle_value)

            if leftmost_value <= rightmost_value:
                # NOTE: A portion with no shift.
                output = min(output, leftmost_value)
                return output
            else:
                # NOTE: A portion with a shift.
                if middle_value >= leftmost_value:
                    L = middle_index + 1
                else:
                    R = middle_index - 1

        return output


def test() -> None:
    array = [
        [4, 5, 6, 7],  # NOTE: No shift.
        [9, 12, 14, 16, 1, 2],  # NOTE: A shift and go right.
        [9, 12, 2, 3, 4, 5, 6],  # NOTE: A shift and go left.
    ]
    for nums in array:
        sol = Solution()
        print(sol.findMin(nums))


if __name__ == "__main__":
    test()

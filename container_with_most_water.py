from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = float("-inf")

        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                left_height = heights[i]
                right_height = heights[j]

                min_height = min(left_height, right_height)
                h = min_height
                w = abs(i - j)
                max_amount = max(max_amount, h * w)

        return max_amount


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = float("-inf")
        L = 0
        R = len(heights) - 1

        while L < R:
            left_height = heights[L]
            right_height = heights[R]

            w = abs(L - R)
            h = min(left_height, right_height)
            max_amount = max(max_amount, h * w)

            if left_height <= right_height:
                L += 1
            else:
                R -= 1

        return max_amount

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        L = 0
        R = len(height) - 1
        max_l = height[L]
        max_r = height[R]
        output = 0

        while L < R:
            if max_l < max_r:
                L += 1
                max_l = max(max_l, height[L])
                output += max_l - height[L]
            else:
                R -= 1
                max_r = max(max_r, height[R])
                output += max_r - height[R]

        return output

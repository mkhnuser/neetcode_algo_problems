from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = float("-inf")
        n = len(heights)

        for i in range(n):
            for j in range(i + 1, n):
                min_height = min(heights[i], heights[j])
                current_volume = min_height * (j - i)
                if current_volume > max_volume:
                    max_volume = current_volume

        return max_volume


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = float("-inf")
        n = len(heights)
        left_pointer = 0
        right_pointer = n - 1

        while left_pointer < right_pointer:
            left_height = heights[left_pointer]
            right_height = heights[right_pointer]
            min_height = min(left_height, right_height)
            area = min_height * (right_pointer - left_pointer)

            if area > max_volume:
                max_volume = area
            if left_height <= right_height:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_volume


def test():
    heights = [1, 7, 2, 5, 4, 7, 3, 6]
    sol = Solution()
    print(sol.maxArea(heights))


if __name__ == "__main__":
    test()

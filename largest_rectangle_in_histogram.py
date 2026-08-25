from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for current_index, current_height in enumerate(heights):
            start = current_index

            while stack and stack[-1][1] > current_height:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (current_index - popped_index))
                start = popped_index

            stack.append([start, current_height])

        for start_index, current_height in stack:
            max_area = max(max_area, current_height * (len(heights) - start_index))

        return max_area

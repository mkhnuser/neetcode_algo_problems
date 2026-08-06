from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_interval = output.pop()
            current_interval = intervals[i]

            if current_interval[0] <= prev_interval[1]:
                merged_interval = [
                    prev_interval[0],
                    max(prev_interval[1], current_interval[1]),
                ]
                output.append(merged_interval)
            else:
                output.append(prev_interval)
                output.append(current_interval)

        return output

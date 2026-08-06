from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # NOTE: The new is completely before the current.
                output.append(newInterval)
                output.extend(intervals[i:])
                return output
            elif newInterval[0] > intervals[i][1]:
                # NOTE: The new if completely after the current.
                output.append(intervals[i])
            else:
                # NOTE: At this point, it's guaraneed that the overlap has happened.
                # ~ (newInterval[1] < intervals[i][0]) and ~ (newInterval[0] > intervals[i][1]) <=>
                # (newInterval[1] >= intervals[i][0]) and (newInterval[0] <= intervals[i][1]).
                # (the end of new interval >= start of an interval) and (the start of the new interval <= end of an interval).
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]

        output.append(newInterval)
        return output

from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()

        s = 0
        e = 0
        current_counter = 0
        max_counter = 0

        while s < len(start) and e < len(end):
            start_time = start[s]
            end_time = end[e]

            if start_time < end_time:
                current_counter += 1
                max_counter = max(max_counter, current_counter)
                s += 1
            else:
                # NOTE: start_time >= end_time.
                current_counter -= 1
                e += 1

        return max_counter

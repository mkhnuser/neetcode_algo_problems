from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            prev_interval = intervals[i - 1]
            if current_interval.start < prev_interval.end:
                return False
        return True


def test() -> None:
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    sol = Solution()
    print(sol.canAttendMeetings(intervals))


if __name__ == "__main__":
    test()

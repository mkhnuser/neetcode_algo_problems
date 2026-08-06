from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        counter = 0
        prev_end = intervals[0][1]

        for current_start, current_end in intervals[1:]:
            if current_start >= prev_end:
                prev_end = current_end
            else:
                counter += 1
                prev_end = min(current_end, prev_end)

        return counter


def test() -> None:
    intervals = [[1, 2], [2, 4], [1, 4]]
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals))

    intervals = [[1, 2], [2, 4]]
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals))


if __name__ == "__main__":
    test()

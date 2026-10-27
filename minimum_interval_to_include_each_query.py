import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        query_to_min_interval_mapping = {}
        interval_index = 0

        for q in sorted(queries):
            while interval_index < len(intervals) and intervals[interval_index][0] <= q:
                l, r = intervals[interval_index]
                heapq.heappush(min_heap, (r - l + 1, r))
                interval_index += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            query_to_min_interval_mapping[q] = min_heap[0][0] if min_heap else -1
        return [query_to_min_interval_mapping[q] for q in queries]

import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # NOTE: Sort by the interval start.
        trips.sort(key=lambda t: t[1])

        min_heap = []  # NOTE: store a pair of [end, numPassengers].
        cur_passengers = 0

        for num, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                cur_passengers -= heapq.heappop(min_heap)[1]

            cur_passengers += num
            if cur_passengers > capacity:
                return False

            heapq.heappush(min_heap, [end, num])

        return True

from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = [i for i in range(n)]
        used_rooms = []  # NOTE: (end time, room number).
        count = [0] * n

        meetings.sort()

        for start, end in meetings:
            while used_rooms and start >= used_rooms[0][0]:
                _, room_number = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room_number)

            # NOTE: Consider two cases.
            # A room is not available.
            # A room is available.

            if not available_rooms:
                end_time, room_number = heapq.heappop(used_rooms)
                end = end_time + (end - start)
                heapq.heappush(available_rooms, room_number)

            room_number = heapq.heappop(available_rooms)
            heapq.heappush(used_rooms, (end, room_number))
            count[room_number] += 1

        return count.index(max(count))

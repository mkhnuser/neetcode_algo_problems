import heapq
from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        adj_mapping = {}

        for flight in flights:
            u, v, w = flight
            if u not in adj_mapping:
                adj_mapping[u] = [[v, w]]
            else:
                adj_mapping[u].append([v, w])

        min_heap = []
        # NOTE: The min heap stores (price, node, number of hops) pairs.
        heapq.heappush(min_heap, (0, src, 0))

        while min_heap:
            current_price, current_node, current_hops = heapq.heappop(min_heap)

            if current_node != dst and current_hops > k:
                continue

            if current_node == dst:
                return current_price

            for neighbor_node, edge_price in adj_mapping.get(current_node, []):
                heapq.heappush(
                    min_heap,
                    (current_price + edge_price, neighbor_node, current_hops + 1),
                )

        return -1

import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_mapping = {}
        points = tuple(tuple(p) for p in points)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                c = points[i]
                p = points[j]

                dist = abs(p[0] - c[0]) + abs(p[1] - c[1])

                if c not in adj_mapping:
                    adj_mapping[c] = [(p, dist)]
                else:
                    adj_mapping[c].append((p, dist))

                if p not in adj_mapping:
                    adj_mapping[p] = [(c, dist)]
                else:
                    adj_mapping[p].append((c, dist))

        starting_point = points[0]
        # NOTE: Store (w, u, v).
        min_heap = []
        visited = set()

        for neighbor_point, edge_weight in adj_mapping.get(starting_point, []):
            if neighbor_point not in visited:
                heapq.heappush(min_heap, (edge_weight, starting_point, neighbor_point))

        visited.add(starting_point)
        output = 0

        while min_heap:
            current_weight, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            output += current_weight

            for neighbor_point, edge_weight in adj_mapping.get(v, []):
                if neighbor_point not in visited:
                    heapq.heappush(min_heap, (edge_weight, v, neighbor_point))

            visited.add(v)

        return output


def test() -> None:
    points = [[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]]
    sol = Solution()
    print(sol.minCostConnectPoints(points))


if __name__ == "__main__":
    test()

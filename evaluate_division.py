from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q = deque()
            visited = set()
            q.append([src, 1])
            visited.add(src)

            while q:
                n, w = q.popleft()

                if n == target:
                    return w

                for neighbor, neighbor_weight in adj.get(n, []):
                    if neighbor not in visited:
                        q.append([neighbor, neighbor_weight * w])
                        visited.add(neighbor)

            return -1

        return [bfs(q[0], q[1]) for q in queries]

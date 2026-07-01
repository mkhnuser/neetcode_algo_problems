from typing import Dict, List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_mapping = {}

        for edge in edges:
            a, b = edge

            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

            if b not in adj_mapping:
                adj_mapping[b] = []
            adj_mapping[b].append(a)

            visited = set()
            if self.has_cycle(adj_mapping, visited, a, None):
                return [a, b]

    def has_cycle(
        self,
        adj_mapping: Dict[int, List[int]],
        visited: set[int],
        n: int,
        p: int | None,
    ) -> bool:
        if n in visited:
            return True

        visited.add(n)

        for g in adj_mapping.get(n, []):
            if g == p:
                continue

            if g in visited:
                return True
            if self.has_cycle(adj_mapping, visited, g, n):
                return True

        return False

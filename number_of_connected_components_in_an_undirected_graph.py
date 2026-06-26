from typing import Dict, List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_mapping = {}

        for edge in edges:
            a, b = edge
            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

            if b not in adj_mapping:
                adj_mapping[b] = []
            adj_mapping[b].append(a)

        colors = [None for _ in range(n)]
        color_pointer = 0

        for v in range(n):
            if colors[v] is None:
                self.dfs(v, adj_mapping, colors, color_pointer)
                color_pointer += 1

        return len(set(colors))

    def dfs(
        self,
        v: int,
        adj_mapping: Dict[int, List[int]],
        colors: List,
        color_pointer: int,
    ) -> None:
        colors[v] = color_pointer

        for g in adj_mapping.get(v, []):
            if colors[g] is None:
                self.dfs(g, adj_mapping, colors, color_pointer)

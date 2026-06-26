from typing import Dict, List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # NOTE:
        # A graph is a valid tree iff:
        # 1. No cycles.
        # 2. The graph consists of only one component.

        adj_mapping = {}

        for edge in edges:
            a, b = edge

            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

            if b not in adj_mapping:
                adj_mapping[b] = []
            adj_mapping[b].append(a)

        colors = ["white" for _ in range(n)]
        has_been_run = False
        parent = None

        for v in range(n):
            if colors[v] == "white":
                if has_been_run:
                    # NOTE: The second component has been found - the graph is disconnected.
                    return False

                if self.is_cycle_present(v, adj_mapping, colors, parent):
                    # NOTE: A cycle has been found.
                    return False

                has_been_run = True

        return True

    def is_cycle_present(
        self,
        v: int,
        adj_mapping: Dict[int, List[int]],
        colors: List[str],
        parent: int | None,
    ) -> bool:
        colors[v] = "gray"

        for n in adj_mapping.get(v, []):
            if n == parent:
                continue

            if colors[n] == "gray":
                return True
            if colors[n] == "white":
                if self.is_cycle_present(n, adj_mapping, colors, v):
                    return True

        colors[v] = "black"
        return False


# NOTE: OK, now try to solve with a visited set.


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_mapping = {}
        visited = set()

        for edge in edges:
            a, b = edge

            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

            if b not in adj_mapping:
                adj_mapping[b] = []
            adj_mapping[b].append(a)

        p = None
        if self.is_cycle_present(p, 0, adj_mapping, visited):
            return False

        return len(visited) == n

    def is_cycle_present(
        self,
        p: int | None,
        v: int,
        adj_mapping: Dict,
        visited: set[int],
    ) -> bool:
        visited.add(v)

        for n in adj_mapping.get(v, []):
            if n == p:
                continue
            if n in visited:
                return True
            if self.is_cycle_present(v, n, adj_mapping, visited):
                return True

        return False

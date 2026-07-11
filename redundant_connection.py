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


class DSU:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.components = n

    def find(self, x: int) -> int:
        p = x
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x: int, y: int) -> bool:
        root_one = self.find(x)
        root_two = self.find(y)

        if root_one == root_two:
            return False

        if self.rank[root_one] > self.rank[root_two]:
            self.parent[root_two] = root_one
        elif self.rank[root_two] > self.rank[root_one]:
            self.parent[root_one] = root_two
        else:
            self.parent[root_two] = root_one
            self.rank[root_one] += 1

        self.components -= 1
        return True

    def get_the_number_of_components(self) -> int:
        return self.components

    def are_in_the_same_component(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)

        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]

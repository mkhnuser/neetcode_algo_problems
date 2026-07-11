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


class DSU:
    def __init__(self, n: int) -> None:
        # NOTE: Let n represent the total number of elements in all disjoint sets.
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.components = n

    def find(self, x: int) -> int:
        # NOTE: Given a node `x`, find its representative.
        p = x
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x: int, y: int) -> bool:
        # NOTE: Return bool which represents whether the union has actually happened.
        root_one = self.find(x)
        root_two = self.find(y)

        if root_one == root_two:
            # NOTE: The elements belong to the same family of elements.
            return False

        # NOTE: OK, now we need to make a union.
        # So, add a tree with a lesser rank to the tree with a larger rank.
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for edge in edges:
            a, b = edge
            dsu.union(a, b)

        return dsu.get_the_number_of_components()

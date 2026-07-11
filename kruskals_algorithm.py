from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
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
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges = [[w, u, v] for u, v, w in edges]
        edges.sort()

        dsu = DSU(n)

        for edge in edges:
            w, u, v = edge
            dsu.union(u, v)

        if dsu.get_the_number_of_components() > 1:
            # NOTE: The graph is not connected.
            # Return -1, as required by the problem statement.
            return -1

        output = 0
        c = 0
        dsu = DSU(n)

        for edge in edges:
            w, u, v = edge

            if not dsu.union(u, v):
                continue

            output += w
            c += 1

            if c == n - 1:
                return output


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda e: e[-1])
        total_weight = 0
        edge_count = 0
        dsu = DSU(n)

        for u, v, w in edges:
            if not dsu.union(u, v):
                continue

            total_weight += w
            edge_count += 1

            if edge_count == n - 1:
                return total_weight

        return -1

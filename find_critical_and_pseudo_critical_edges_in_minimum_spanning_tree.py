import heapq
from typing import Dict, List


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
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]],
    ) -> List[List[int]]:
        for i, edge in enumerate(edges):
            # NOTE: Preserve the original edge index for the future.
            edge.append(i)

        # NOTE: Sort edges based on their weight.
        edges.sort(key=lambda e: e[-2])

        # NOTE: Store <u: (v, weight), v: (u, weight)>.
        adj_mapping = {}

        for edge in edges:
            u, v, w, i = edge

            if u not in adj_mapping:
                adj_mapping[u] = [(v, w)]
            else:
                adj_mapping[u].append((v, w))

            if v not in adj_mapping:
                adj_mapping[v] = [(u, w)]
            else:
                adj_mapping[v].append((u, w))

        reference_weight = self.prim(adj_mapping)
        output = [[], []]

        for i in range(len(edges)):
            w1 = self.kruskal(n, edges, exclude_index=i)
            w2 = self.kruskal(n, edges, include_index=i)
            if w1 > reference_weight:
                # NOTE: We include the original index.
                output[0].append(edges[i][-1])
            elif w2 == reference_weight:
                # NOTE: We include the original index.
                output[1].append(edges[i][-1])

        return output

    def prim(self, adj_mapping: Dict) -> int:
        # NOTE: Vertices are from 0 to n - 1.
        starting_vertex = 0
        min_heap = []  # NOTE: (w, u, v).
        visited = set()
        visited.add(starting_vertex)
        mst_weight = 0

        for vertex_two, weight in adj_mapping.get(starting_vertex, []):
            heapq.heappush(min_heap, (weight, starting_vertex, vertex_two))

        while min_heap:
            w, u, v = heapq.heappop(min_heap)

            if v in visited:
                # NOTE: v is already present in the MST.
                continue

            mst_weight += w

            for vertex_two, weight in adj_mapping.get(v, []):
                if vertex_two not in visited:
                    heapq.heappush(min_heap, (weight, v, vertex_two))

            visited.add(v)

        return mst_weight

    def kruskal(
        self,
        n: int,
        edges: List[List[int]],
        exclude_index: int = -1,
        include_index: int = -1,
    ) -> int:
        mst_weight = 0
        dsu = DSU(n)

        if include_index != -1:
            mst_weight += edges[include_index][-2]
            dsu.union(edges[include_index][0], edges[include_index][1])

        for i, edge in enumerate(edges):
            a, b, w, _ = edge

            if i == exclude_index:
                continue

            if not dsu.union(a, b):
                continue

            mst_weight += w

        return mst_weight if dsu.get_the_number_of_components() == 1 else float("+inf")


def test() -> None:
    n = 4
    edges = [[0, 3, 2], [0, 2, 5], [1, 2, 4]]
    sol = Solution()
    print(sol.findCriticalAndPseudoCriticalEdges(n, edges))

    n = 5
    edges = [
        [0, 3, 2],
        [0, 4, 2],
        [1, 3, 2],
        [3, 4, 2],
        [2, 3, 1],
        [1, 2, 3],
        [0, 1, 1],
    ]
    sol = Solution()
    print(sol.findCriticalAndPseudoCriticalEdges(n, edges))


if __name__ == "__main__":
    test()

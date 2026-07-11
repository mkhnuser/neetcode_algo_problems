class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = {}
        self.rank = {}
        self.number_of_components = 0

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
            self.number_of_components += 1

    def find(self, x: int) -> int:
        # NOTE: While p is not self-parent (the root), go up the chain.
        # Also, compress the upward path.
        p = x
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        # NOTE: Check whether the nodes share the same root.
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_one = self.find(x)
        root_two = self.find(y)

        if root_one == root_two:
            return False

        if self.rank[root_one] > self.rank[root_two]:
            self.parent[root_two] = root_one
        elif self.rank[root_one] < self.rank[root_two]:
            self.parent[root_one] = root_two
        else:
            self.parent[root_two] = root_one
            self.rank[root_one] += 1

        self.number_of_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.number_of_components

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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        union_find = DSU(len(nums))

        factor_to_index_mapping = {}

        for i, n in enumerate(nums):
            factor = 2
            while factor * factor <= n:
                if n % factor == 0:
                    if factor in factor_to_index_mapping:
                        union_find.union(i, factor_to_index_mapping[factor])
                    else:
                        factor_to_index_mapping[factor] = i
                    while n % factor == 0:
                        n //= factor
                factor += 1

            if n > 1:
                if n in factor_to_index_mapping:
                    union_find.union(i, factor_to_index_mapping[n])
                else:
                    factor_to_index_mapping[n] = i

        return union_find.get_the_number_of_components() == 1

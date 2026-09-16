from typing import List, MutableMapping


# NOTE: rowConditions = [[above, below], ...].
# NOTE: colConditions = [[left, right], ...].

# NOTE:
# Input: k = 3, rowConditions = [[2,1],[1,3]], colConditions = [[3,1],[2,3]].
# [
#     [2, 0, 0],
#     [0, 0, 1],
#     [0, 3, 0],
# ].

# TODO: Use topological ordering.
# Input: k = 3, rowConditions = [[2,1],[1,3]], colConditions = [[3,1],[2,3]].
# Topological ordering for rows: 2 -> 1 -> 3.
# Topological ordering for cols: 2 -> 3 -> 1.

# NOTE:
# Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]].
# Input: k = 3, rowConditions = [[1,2],[2,3],[3,1]], colConditions = [[2,1]].
# [].
# WARNING: There is a cycle, so return [].


class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> List[List[int]]:
        rows_adj_mapping = {}
        cols_adj_mapping = {}

        self.create_adj_mapping(rows_adj_mapping, rowConditions)
        self.create_adj_mapping(cols_adj_mapping, colConditions)

        rows_colors = ["white"] * k
        cols_colors = ["white"] * k

        for v in range(1, k + 1):
            if rows_colors[v - 1] == "white":
                if self.has_cycle(v, rows_adj_mapping, rows_colors):
                    return []

            if cols_colors[v - 1] == "white":
                if self.has_cycle(v, cols_adj_mapping, cols_colors):
                    return []

        rows_ordering = []
        cols_ordering = []

        for ordering, adj_mapping in (
            (rows_ordering, rows_adj_mapping),
            (cols_ordering, cols_adj_mapping),
        ):
            visited = set()
            for v in range(1, k + 1):
                if v not in visited:
                    self.obtain_topological_order(
                        v,
                        adj_mapping,
                        visited,
                        ordering,
                    )

            ordering.reverse()

        matrix = [[0 for _ in range(k)] for __ in range(k)]

        row_position = {}
        for i, row_num in enumerate(rows_ordering):
            row_position[row_num] = i

        col_position = {}
        for j, col_num in enumerate(cols_ordering):
            col_position[col_num] = j

        for x in range(1, k + 1):
            matrix[row_position[x]][col_position[x]] = x

        return matrix

    def obtain_topological_order(
        self,
        v: int,
        mapping: MutableMapping,
        visited: set[int],
        ordering: list[int],
    ) -> None:
        visited.add(v)

        for n in mapping.get(v, []):
            if n not in visited:
                self.obtain_topological_order(n, mapping, visited, ordering)

        ordering.append(v)

    def has_cycle(
        self,
        v: int,
        mapping: MutableMapping,
        colors: list[str],
    ) -> bool:
        colors[v - 1] = "gray"

        for n in mapping.get(v, []):
            if colors[n - 1] == "gray":
                return True

            if colors[n - 1] == "black":
                continue

            if self.has_cycle(n, mapping, colors):
                return True

        colors[v - 1] = "black"
        return False

    def create_adj_mapping(
        self,
        mapping: MutableMapping[int, set[int]],
        conditions: List[List[int]],
    ) -> None:
        for cond in conditions:
            a, b = cond
            if a not in mapping:
                mapping[a] = set()
            mapping[a].add(b)


def test() -> None:
    k = 3
    rowConditions = [[2, 1], [1, 3]]
    colConditions = [[3, 1], [2, 3]]
    sol = Solution()
    print(sol.buildMatrix(k, rowConditions, colConditions))

    k = 3
    rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
    colConditions = [[2, 1]]
    sol = Solution()
    print(sol.buildMatrix(k, rowConditions, colConditions))

    k = 3
    rowConditions = [[1, 2], [3, 2]]
    colConditions = [[2, 1], [3, 2]]
    sol = Solution()
    print(sol.buildMatrix(k, rowConditions, colConditions))


if __name__ == "__main__":
    test()

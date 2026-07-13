from typing import List, Literal, Dict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # NOTE: First ensure the graph is a DAG.
        # Understand: the graph might not be connected.
        colors: List[Literal["white", "gray", "black"]] = [
            "white" for _ in range(numCourses)
        ]

        adj_mapping = {}
        for p in prerequisites:
            a, b = p
            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

        for v in range(numCourses):
            if colors[v] == "white":
                if self.has_cycle(v, adj_mapping, colors):
                    return []

        # NOTE: At this point, there are no cycles in the graph, so topological ordering can be obtained.
        colors: List[Literal["white", "gray", "black"]] = [
            "white" for _ in range(numCourses)
        ]
        reverse_topological_order = []

        for v in range(numCourses):
            if colors[v] == "white":
                self.reverse_topologically_sort(
                    v,
                    adj_mapping,
                    colors,
                    reverse_topological_order,
                )

        return reverse_topological_order

    def has_cycle(self, v: int, adj_mapping: Dict, colors: List) -> bool:
        colors[v] = "gray"

        for n in adj_mapping.get(v, []):
            if colors[n] == "gray":
                return True

            if colors[n] == "white":
                if self.has_cycle(n, adj_mapping, colors):
                    return True

        colors[v] = "black"
        return False

    def reverse_topologically_sort(
        self,
        v: int,
        adj_mapping: Dict,
        colors: List,
        reverse_topological_order: List,
    ) -> None:
        colors[v] = "gray"

        for n in adj_mapping.get(v, []):
            if colors[n] == "white":
                self.reverse_topologically_sort(
                    n, adj_mapping, colors, reverse_topological_order
                )

        colors[v] = "black"
        reverse_topological_order.append(v)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # NOTE: First ensure the graph is a DAG.
        # Understand: the graph might not be connected.
        colors: List[Literal["white", "gray", "black"]] = [
            "white" for _ in range(numCourses)
        ]

        adj_mapping = {}
        for p in prerequisites:
            a, b = p
            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

        reverse_topological_order = []
        for v in range(numCourses):
            if colors[v] == "white":
                if self.dfs(v, adj_mapping, colors, reverse_topological_order):
                    return []
        return reverse_topological_order

    def dfs(
        self,
        v: int,
        adj_mapping: Dict,
        colors: List,
        reverse_topological_order: List,
    ) -> bool:
        """Return `True` if there is a cycle, return `False` otherwise.

        If there is no cycle, a reverse topological order is constructed.
        """
        colors[v] = "gray"

        for n in adj_mapping.get(v, []):
            if colors[n] == "gray":
                return True

            if colors[n] == "white":
                if self.dfs(n, adj_mapping, colors, reverse_topological_order):
                    return True

        colors[v] = "black"
        reverse_topological_order.append(v)
        return False

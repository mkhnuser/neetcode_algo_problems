from typing import List, Literal, Dict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # NOTE: Courses are represented as 0 .. numCourses - 1.
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
                    return False
        return True

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

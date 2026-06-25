from typing import List, Literal, Dict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        colors: List[
            Literal[
                "white",
                "gray",
                "black",
            ]
        ] = ["white" for _ in range(numCourses)]
        adj_mapping = {}

        # NOTE: Let's represent a depends on b relationship.
        for a, b in prerequisites:
            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

        for c in adj_mapping:
            if colors[c] == "white":
                if self.has_cycle(c, adj_mapping, colors):
                    return False

        return True

    def has_cycle(
        self,
        c: int,
        adj_mapping: Dict[int, List[int]],
        colors: List[Literal["white", "gray", "black"]],
    ) -> bool:
        colors[c] = "gray"

        for g in adj_mapping.get(c, []):
            if colors[g] == "gray":
                return True

            if colors[g] == "white":
                if self.has_cycle(g, adj_mapping, colors):
                    return True

        colors[c] = "black"
        return False

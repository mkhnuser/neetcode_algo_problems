from typing import List, Literal, Dict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        output = []

        for c in range(numCourses):
            if colors[c] == "white":
                if self.dfs(c, adj_mapping, colors, output):
                    return []

        return output

    def dfs(
        self,
        c: int,
        adj_mapping: Dict[int, List[int]],
        colors: List[Literal["white", "gray", "black"]],
        output: list[int],
    ) -> bool:
        colors[c] = "gray"

        for g in adj_mapping.get(c, []):
            if colors[g] == "gray":
                return True

            if colors[g] == "white":
                if self.dfs(g, adj_mapping, colors, output):
                    return True

        colors[c] = "black"
        output.append(c)
        return False


def test():
    sol = Solution()
    print(sol.findOrder(2, [[1, 0]]))


if __name__ == "__main__":
    test()

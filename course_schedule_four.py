from typing import Dict, List


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adj_mapping = {}

        # NOTE: Represent: prereq -> course.
        for a, b in prerequisites:
            if a not in adj_mapping:
                adj_mapping[a] = []
            adj_mapping[a].append(b)

        output = []
        for query in queries:
            u, v = query
            visited = set()
            path = set()
            # NOTE: Can v be reaced starting from u?
            output.append(self.can_be_reached(v, u, adj_mapping, visited, path))
        return output

    def can_be_reached(
        self,
        v: int,
        u: int,
        adj_mapping: Dict,
        visited: set,
        path: set,
    ) -> bool:
        if u == v:
            return True

        path.add(u)
        visited.add(u)

        for n in adj_mapping.get(u, []):
            if n in path:
                # NOTE: We've already had n on out path,
                # NOTE: so a cycle has been detected.
                return False

            if n not in visited:
                if self.can_be_reached(v, n, adj_mapping, visited, path):
                    return True

        path.remove(u)
        return False


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adj_mapping = {}

        # NOTE: Represent: course -> prereq.
        for a, b in prerequisites:
            if b not in adj_mapping:
                adj_mapping[b] = []
            adj_mapping[b].append(a)

        prereq_mapping = {}
        for v in range(numCourses):
            self.dfs(
                v,
                adj_mapping,
                prereq_mapping,
            )

        output = []
        for query in queries:
            u, v = query
            output.append(u in prereq_mapping[v])
        return output

    def dfs(
        self,
        u: int,
        adj_mapping: Dict,
        prereq_mapping: Dict,
    ) -> bool:
        if u not in prereq_mapping:
            prereq_mapping[u] = set()

            for n in adj_mapping.get(u, []):
                prereq_mapping[u].update(self.dfs(n, adj_mapping, prereq_mapping))

            prereq_mapping[u].add(u)
        return prereq_mapping[u]


def test() -> None:
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    queries = [[0, 1], [3, 1]]
    sol = Solution()
    print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))
    numCourses = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1]]
    sol = Solution()
    print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))


if __name__ == "__main__":
    test()

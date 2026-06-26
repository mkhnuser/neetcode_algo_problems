from typing import Dict, List
from queue import Queue


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

        answer = []

        for u, v in queries:
            # NOTE: Can we reach v from u?
            answer.append(self.can_be_reached(v, u, adj_mapping))

        return answer

    def can_be_reached(self, v: int, u: int, adj_mapping: Dict) -> bool:
        q = Queue()
        q.put(u)
        visited = set()
        visited.add(u)

        while q.qsize() > 0:
            c = q.get()

            if c == v:
                return True

            for n in adj_mapping.get(c, []):
                if n not in visited:
                    q.put(n)
                    visited.add(n)

        return False

from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_mapping = {src: [] for src, dst in tickets}

        for src, dst in tickets:
            adj_mapping[src].append(dst)

        starting_vertex = "JFK"
        res = [starting_vertex]

        def dfs(src: str) -> bool:
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj_mapping:
                # NOTE: A dead end has been reached.
                return False

            for i, n in enumerate(adj_mapping[src]):
                if n == -1:
                    # NOTE: This airport has already been visited in the current path.
                    continue

                adj_mapping[src][i] = -1
                res.append(n)

                if dfs(n):
                    return True

                adj_mapping[src][i] = n
                res.pop()

            # NOTE: No outgoing edges: a dead end has been reached.
            return False

        dfs(starting_vertex)
        return res

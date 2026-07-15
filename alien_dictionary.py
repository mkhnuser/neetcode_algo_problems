from typing import List, Dict


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_mapping = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_mapping[w1[j]].add(w2[j])
                    break

        reverse_topological_order = []
        visited = set()

        for c in adj_mapping:
            path = set()
            if c not in visited:
                if self.dfs(c, adj_mapping, visited, path, reverse_topological_order):
                    return ""

        return "".join(reversed(reverse_topological_order))

    def dfs(
        self,
        v: str,
        adj_mapping: Dict,
        visited: set,
        path: set,
        reverse_topological_order: list,
    ) -> bool:
        path.add(v)
        visited.add(v)

        for n in adj_mapping.get(v, []):
            if n in path:
                # NOTE: We've already had n on out path,
                # NOTE: so a cycle has been detected.
                return True

            if n not in visited:
                if self.dfs(n, adj_mapping, visited, path, reverse_topological_order):
                    return True

        path.remove(v)
        reverse_topological_order.append(v)
        return False


def test() -> None:
    words = ["z", "o"]
    sol = Solution()
    print(sol.foreignDictionary(words))

    words = ["hrn", "hrf", "er", "enn", "rfnn"]
    sol = Solution()
    print(sol.foreignDictionary(words))

    words = ["abc", "ab"]
    sol = Solution()
    print(sol.foreignDictionary(words))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # NOTE: At most m 0's and n 1's.
        memo = {}
        i = 0
        return self.recurse(strs, memo, i, m, n)

    def recurse(self, strs: List[str], memo: dict, i: int, m: int, n: int) -> int:
        if i >= len(strs):
            return 0
        if (i, m, n) in memo:
            return memo[(i, m, n)]

        s = strs[i]
        m_count = s.count("0")
        n_count = s.count("1")
        memo[(i, m, n)] = self.recurse(strs, memo, i + 1, m, n)

        if m_count <= m and n_count <= n:
            memo[(i, m, n)] = max(
                memo[(i, m, n)],
                1 + self.recurse(strs, memo, i + 1, m - m_count, n - n_count),
            )
        return memo[(i, m, n)]

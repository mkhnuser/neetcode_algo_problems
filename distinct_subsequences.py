from typing import MutableMapping


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.recurse(s, t, 0, [])

    def recurse(self, s: str, t: str, i: int, seq: list[str]) -> int:
        if i >= len(s):
            return 1 if "".join(seq) == t else 0

        seq.append(s[i])
        inclusive_path = self.recurse(s, t, i + 1, seq)
        seq.pop()
        exclusive_path = self.recurse(s, t, i + 1, seq)
        return inclusive_path + exclusive_path


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.recurse(s, t, 0, [], {})

    def recurse(
        self,
        s: str,
        t: str,
        i: int,
        seq: list[str],
        cache: MutableMapping[tuple[int, tuple[str, ...]], int],
    ) -> int:
        if i >= len(s):
            return 1 if "".join(seq) == t else 0

        # NOTE: Let cache[cache_key] answer the question:
        # Starting from index i and having a concrete sequence, what number of sequences can be obtained further?
        cache_key = (i, tuple(seq))
        if cache_key in cache:
            return cache[cache_key]

        seq.append(s[i])
        inclusive_path = self.recurse(s, t, i + 1, seq, cache)
        seq.pop()
        exclusive_path = self.recurse(s, t, i + 1, seq, cache)
        cache[cache_key] = inclusive_path + exclusive_path
        return cache[cache_key]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.recurse(s, t, 0, 0, {}, len(s), len(t))

    def recurse(
        self,
        s: str,
        t: str,
        i: int,
        j: int,
        cache: MutableMapping[tuple[int, int], int],
        n: int,
        m: int,
    ) -> int:
        if j >= m:
            return 1
        if i >= n:
            return 0

        # NOTE: Let cache[(i, j)] represent:
        # Given s[i:] and t[j:], what number of subsequences can be obtained from s[i:] to create t[j:]?
        cache_key = (i, j)
        if (i, j) in cache:
            return cache[cache_key]

        if s[i] == t[j]:
            cache[cache_key] = self.recurse(
                s,
                t,
                i + 1,
                j + 1,
                cache,
                n,
                m,
            ) + self.recurse(
                s,
                t,
                i + 1,
                j,
                cache,
                n,
                m,
            )
        else:
            cache[cache_key] = self.recurse(s, t, i + 1, j, cache, n, m)

        return cache[cache_key]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        # NOTE: Let dp[i][j] answer the question:
        # - Given suffixes s[i:] and t[j:], how many subsequences does s[i:] contain which form t[j:]?
        dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

        for j in range(m + 1):
            dp[-1][j] = 0

        for i in range(n + 1):
            dp[i][-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        # NOTE: Let dp[i][j] answer the question:
        # - Given suffixes s[i:] and t[j:], how many subsequences does s[i:] contain which form t[j:]?
        dp = [0 for _ in range(m + 1)]
        dp[-1] = 1

        for i in range(n - 1, -1, -1):
            current_dp_row = [0 for _ in range(m + 1)]
            current_dp_row[-1] = 1

            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    current_dp_row[j] = dp[j] + dp[j + 1]
                else:
                    current_dp_row[j] = dp[j]

            dp = current_dp_row

        return dp[0]


def test() -> None:
    sol = Solution()
    print(sol.numDistinct("caaat", "cat"))


if __name__ == "__main__":
    test()

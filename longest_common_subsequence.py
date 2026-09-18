from typing import MutableMapping


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = text1
        b = text2
        return self.recurse(a, b, 0, 0)

    def recurse(self, a: str, b: str, i: int, j: int) -> int:
        if i >= len(a) or j >= len(b):
            return 0

        if a[i] != b[j]:
            return max(self.recurse(a, b, i + 1, j), self.recurse(a, b, i, j + 1))
        return 1 + self.recurse(a, b, i + 1, j + 1)


from typing import MutableMapping


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = text1
        b = text2
        return self.recurse(a, b, 0, 0, {})

    def recurse(
        self,
        a: str,
        b: str,
        i: int,
        j: int,
        cache: MutableMapping[tuple[int, int], int],
    ) -> int:
        if i >= len(a) or j >= len(b):
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        if a[i] != b[j]:
            cache[(i, j)] = max(
                self.recurse(a, b, i + 1, j, cache),
                self.recurse(a, b, i, j + 1, cache),
            )
            return cache[(i, j)]

        cache[(i, j)] = 1 + self.recurse(a, b, i + 1, j + 1, cache)
        return cache[(i, j)]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = text1
        b = text2

        # NOTE: Let dp[i][j] answer the question:
        # - What's the LCS between strings a[i:] and b[j:]?
        dp = [[0 for _ in range(len(b) + 1)] for __ in range(len(a) + 1)]

        # NOTE:
        # Suppose a = "dept", b = "cat".
        # Then len(a) == 4 and len(b) == 3.
        # Then initial dp equals:
        # / 0 1 2 -
        # 0 0 0 0 0
        # 1 0 0 0 0
        # 2 0 0 0 0
        # 3 0 0 0 0
        # | 0 0 0

        # NOTE: What's the LCS between a[3:] and b[2:]?
        # If the chars are equal, then 1, and 0 otherwise.

        dp[len(a) - 1][len(b) - 1] = 1 if a[len(a) - 1] == b[len(b) - 1] else 0

        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                if a[i] != b[j]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
        # NOTE:
        # Then final dp equals:
        # / 0 1 2 -
        # 0 1 1 1 0
        # 1 1 1 1 0
        # 2 1 1 1 0
        # 3 1 1 1 0
        # | 0 0 0

        return dp[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = text1
        b = text2
        n = len(a)
        m = len(b)

        # NOTE: Let dp[i][j] answer the question:
        # - What's the LCS between strings a[i:] and b[j:]?
        dp = [0 for _ in range(m + 1)]
        dp[m - 1] = 1 if a[n - 1] == b[m - 1] else 0

        for i in range(n - 1, -1, -1):
            current_dp_row = [0 for _ in range(m + 1)]

            for j in range(m - 1, -1, -1):
                if a[i] != b[j]:
                    current_dp_row[j] = max(current_dp_row[j + 1], dp[j])
                else:
                    current_dp_row[j] = 1 + dp[j + 1]

            dp = current_dp_row

        return dp[0]


def test() -> None:
    text1 = "cat"
    text2 = "crabt"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))

    text1 = "abcd"
    text2 = "abcd"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))

    text1 = "abcd"
    text2 = "efgh"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))


if __name__ == "__main__":
    test()

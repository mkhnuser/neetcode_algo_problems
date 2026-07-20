class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dfs(0, 0, text1, text2, {})

    def dfs(self, i: int, j: int, text1: str, text2: str, cache: dict) -> int:
        # NOTE: i points to text1; j points to text2.
        if i >= len(text1) or j >= len(text2):
            return 0
        if text1[i] == text2[j]:
            cache[(i, j)] = 1 + self.dfs(i + 1, j + 1, text1, text2, cache)
            return cache[(i, j)]
        if (i, j) in cache:
            return cache[(i, j)]

        max_subsequence_length = max(
            self.dfs(i + 1, j, text1, text2, cache),
            self.dfs(i, j + 1, text1, text2, cache),
        )
        cache[(i, j)] = max_subsequence_length
        return cache[(i, j)]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)

        dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)]

        for i in range(N):
            for j in range(M):
                if text1[i] == text2[j]:
                    # NOTE: Increase LCS by one.
                    # dp[i][j] represents LCS between text1[:i] and text2[:j].
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    # NOTE:
                    # dp[i][j + 1] represents LCS between text1[:i] and text2[:j + 1].
                    # dp[i + 1][j] represents LCS between text1[:i + 1] and text2[:j].
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[N][M]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)

        dp = [0 for _ in range(M + 1)]

        for i in range(N):
            cur_row = [0 for _ in range(M + 1)]
            for j in range(M):
                if text1[i] == text2[j]:
                    cur_row[j + 1] = 1 + dp[j]
                else:
                    cur_row[j + 1] = max(dp[j + 1], cur_row[j])
            dp = cur_row

        return dp[M]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)

        dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


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

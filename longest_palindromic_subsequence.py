class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])

    def lcs(self, s1: str, s2: str) -> int:
        M = len(s1)
        N = len(s2)

        # NOTE: Let dp[i][j] represent the LCS between suffixes s2[i:] and s1[j:].

        dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s2[i] == s1[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

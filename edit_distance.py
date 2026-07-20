class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # NOTE: An objective: transform word1 into word2.
        return self.recurse(word1, word2, 0, 0, {})

    def recurse(self, word1: str, word2: str, i: int, j: int, cache: dict) -> int:
        if i >= len(word1):
            return len(word2) - j
        if j >= len(word2):
            return len(word1) - i

        if (i, j) in cache:
            return cache[(i, j)]

        if word1[i] == word2[j]:
            cache[(i, j)] = self.recurse(word1, word2, i + 1, j + 1, cache)
            return cache[(i, j)]
        else:
            # NOTE:
            # 1. Insert.
            # 2. Delete.
            # 3. Replace.

            insertion_recursion = self.recurse(word1, word2, i, j + 1, cache)
            deletion_recursion = self.recurse(word1, word2, i + 1, j, cache)
            replacement_recursion = self.recurse(word1, word2, i + 1, j + 1, cache)

            cache[(i, j)] = 1 + min(
                insertion_recursion,
                deletion_recursion,
                replacement_recursion,
            )

            return cache[(i, j)]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2)

    def dp(self, word1: str, word2: str) -> int:
        # NOTE:
        # 1. Insert.
        # 2. Delete.
        # 3. Replace.
        M = len(word1)
        N = len(word2)
        dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)]

        for i in range(N):
            dp[i][-1] = N - i

        for j in range(M):
            dp[-1][j] = M - j

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2)

    def dp(self, word1: str, word2: str) -> int:
        # NOTE:
        # 1. Insert.
        # 2. Delete.
        # 3. Replace.
        M = len(word1)
        N = len(word2)

        dp = [0 for _ in range(M + 1)]
        for j in range(M):
            dp[j] = M - j

        for i in range(N - 1, -1, -1):
            cur_row = [0 for _ in range(M + 1)]
            cur_row[-1] = N - i

            for j in range(M - 1, -1, -1):
                if word1[j] == word2[i]:
                    cur_row[j] = dp[j + 1]
                else:
                    cur_row[j] = 1 + min(dp[j], dp[j + 1], cur_row[j + 1])

            dp = cur_row

        return dp[0]


def test() -> None:
    sol = Solution()
    print(sol.minDistance("ab", "az"))
    sol = Solution()
    print(sol.minDistance("a", "a"))


if __name__ == "__main__":
    test()

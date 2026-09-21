class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    return True

            return False

        return dfs(0, 0, 0)


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        z = len(s3)

        if n + m != z:
            return False

        def dfs(i, j, k, cache):
            if k == z:
                return (i == n) and (j == m)

            # NOTE: Let cache[(i, j, k)] answer the question:
            # - Given s1[i:] and s2[j:], is it possible to form s3[k:] by interleaving?

            triplet = (i, j, k)
            if triplet in cache:
                return cache[triplet]

            if i < n and s1[i] == s3[k]:
                cache[triplet] = dfs(i + 1, j, k + 1, cache)
                if cache[triplet]:
                    return True

            if j < m and s2[j] == s3[k]:
                cache[triplet] = dfs(i, j + 1, k + 1, cache)
                if cache[triplet]:
                    return True

            return False

        return dfs(0, 0, 0, {})


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        z = len(s3)

        if n + m != z:
            return False

        # NOTE: Let dp[i][j] answer the question:
        # - Starting from s1[i:] and s2[j:], is it possible to form s3[i + j:] by interleaving?
        dp = [[False for _ in range(m + 1)] for __ in range(n + 1)]
        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                k = i + j
                if i < n and s1[i] == s3[k] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < m and s2[j] == s3[k] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


def test() -> None:
    s1 = "aaaa"
    s2 = "bbbb"
    s3 = "aabbbbaa"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))

    s1 = ""
    s2 = ""
    s3 = ""
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))

    s1 = "abc"
    s2 = "xyz"
    s3 = "abxzcy"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))


if __name__ == "__main__":
    test()

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True

        i = 0
        j = 0
        k = 0
        return self.recurse(s1, s2, s3, i, j, k, {})

    def recurse(
        self,
        s1: str,
        s2: str,
        s3: str,
        i: int,
        j: int,
        k: int,
        memo: dict,
    ) -> bool:
        if k >= len(s3):
            return (i >= len(s1)) and (j >= len(s2))

        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i < len(s1) and s1[i] == s3[k]:
            rec = self.recurse(s1, s2, s3, i + 1, j, k + 1, memo)
            memo[(i + 1, j, k + 1)] = rec
            if rec:
                return True

        if j < len(s2) and s2[j] == s3[k]:
            rec = self.recurse(s1, s2, s3, i, j + 1, k + 1, memo)
            memo[(i, j + 1, k + 1)] = rec
            if rec:
                return True

        return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if len(s3) != len(s1) + len(s2):
            return False

        return self.dp(s1, s2, s3)

    def dp(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)

        dp = [[False for _ in range(M + 1)] for __ in range(N + 1)]
        dp[-1][-1] = True

        for i in range(N, -1, -1):
            for j in range(M, -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
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


if __name__ == "__main__":
    test()

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        return self.recurse(0, 0, str1, str2)

    def recurse(self, i: int, j: int, str1: str, str2: str) -> str:
        if i >= len(str1):
            return str2[j:]
        if j >= len(str2):
            return str1[i:]

        if str1[i] == str2[j]:
            return str1[i] + self.recurse(i + 1, j + 1, str1, str2)

        path_one = str1[i] + self.recurse(i + 1, j, str1, str2)
        path_two = str2[j] + self.recurse(i, j + 1, str1, str2)
        return min(path_one, path_two, key=len)


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        return self.recurse(0, 0, str1, str2, {})

    def recurse(self, i: int, j: int, str1: str, str2: str, cache: dict) -> str:
        if i >= len(str1):
            return str2[j:]
        if j >= len(str2):
            return str1[i:]

        # NOTE: Let the cache answer the question:
        # Given suffixes str1[i:] and str2[j:], what's the minimum supersequence which contains these two suffixes?
        if (i, j) in cache:
            return cache[(i, j)]

        if str1[i] == str2[j]:
            cache[(i, j)] = str1[i] + self.recurse(i + 1, j + 1, str1, str2, cache)
            return cache[(i, j)]

        path_one = str1[i] + self.recurse(i + 1, j, str1, str2, cache)
        path_two = str2[j] + self.recurse(i, j + 1, str1, str2, cache)
        cache[(i, j)] = min(path_one, path_two, key=len)
        return cache[(i, j)]


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        # NOTE: Let dp[i][j] answer question:
        # Given suffixes str1[i:] and str2[j:], what's the minimum supersequence which contains these two suffixes?
        dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
        dp[-1][-1] = ""

        for j in range(m):
            dp[-1][j] = str2[j:]

        for i in range(n):
            dp[i][-1] = str1[i:]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    path_one = str1[i] + dp[i + 1][j]
                    path_two = str2[j] + dp[i][j + 1]
                    dp[i][j] = min(path_one, path_two, key=len)

        return dp[0][0]


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = ["" for _ in range(m + 1)]

        for j in range(m):
            dp[j] = str2[j:]

        for i in range(n - 1, -1, -1):
            current_dp_row = ["" for _ in range(m + 1)]

            for j in range(m, -1, -1):
                if j == m:
                    current_dp_row[j] = str1[i:]
                    continue

                if str1[i] == str2[j]:
                    current_dp_row[j] = str1[i] + dp[j + 1]
                else:
                    path_one = str1[i] + dp[j]
                    path_two = str2[j] + current_dp_row[j + 1]
                    current_dp_row[j] = min(path_one, path_two, key=len)

            dp = current_dp_row

        return dp[0]


def test() -> None:
    sol = Solution()
    print(sol.shortestCommonSupersequence("abac", "cab"))


if __name__ == "__main__":
    test()

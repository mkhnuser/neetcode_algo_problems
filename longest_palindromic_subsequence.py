class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.recurse(s, 0, [], len(s))

    def recurse(self, s: str, i: int, c: list[str], n: int) -> int:
        if i >= n:
            return len(c) if self.is_pal("".join(c)) else 0

        c.append(s[i])
        inclusive_path = self.recurse(s, i + 1, c, n)
        c.pop()
        exclusive_path = self.recurse(s, i + 1, c, n)
        return max(inclusive_path, exclusive_path)

    def is_pal(self, candidate: str) -> bool:
        L = 0
        R = len(candidate) - 1

        while L < R:
            if candidate[L] != candidate[R]:
                return False
            L += 1
            R -= 1

        return True


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                cache[(i, j)] = dfs(i + 1, j - 1) + 2
            else:
                cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j - 1))

            return cache[(i, j)]

        return dfs(0, len(s) - 1)


def test() -> None:
    s = "bbbab"
    sol = Solution()
    print(sol.longestPalindromeSubseq(s))

    s = "cbbd"
    sol = Solution()
    print(sol.longestPalindromeSubseq(s))


if __name__ == "__main__":
    test()

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        output = 0

        for i in range(n):
            L = R = i

            while 0 <= L and R <= n - 1 and s[L] == s[R]:
                output += 1
                L -= 1
                R += 1

            L = R = i
            L -= 1

            while 0 <= L and R <= n - 1 and s[L] == s[R]:
                output += 1
                L -= 1
                R += 1

        return output


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        output = 0

        # NOTE: Let dp[i][j] answer the question: is s[i:j + 1] a palindrome?
        dp = [[False for _ in range(n)] for __ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    output += 1
        # NOTE:
        #     0123
        #   \ abbc
        # 0 a T...
        # 1 b .TT.
        # 2 b ..T.
        # 3 c ...T

        return output


def test() -> None:
    sol = Solution()
    print(sol.countSubstrings("abbc"))


if __name__ == "__main__":
    test()

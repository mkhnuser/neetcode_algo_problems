class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("+inf") for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        for t in range(1, n + 1):
            for q in range(1, t + 1):
                s = q**2

                if t < s:
                    break

                dp[t] = min(dp[t], 1 + dp[t - s])

        return dp[n]


def test() -> None:
    sol = Solution()
    print(sol.numSquares(13))
    sol = Solution()
    print(sol.numSquares(6))
    sol = Solution()
    print(sol.numSquares(12))


if __name__ == "__main__":
    test()

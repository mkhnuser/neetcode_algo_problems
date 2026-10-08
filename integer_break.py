class Solution:
    def integerBreak(self, n: int) -> int:
        return self.recurse(n, n, {})

    def recurse(
        self,
        initial_n: int,
        n: int,
        memo: dict,
    ) -> int:
        if n == 1:
            return 1

        # NOTE: memo[n] answers the question:
        # Given an int `n`, what's the max product split that can be obtained?
        if n in memo:
            return memo[n]

        output = 0 if n == initial_n else n

        for i in range(1, n):
            output = max(
                output,
                self.recurse(initial_n, i, memo) * self.recurse(initial_n, n - i, memo),
            )
        memo[n] = output
        return memo[n]


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float("-inf") for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        for t in range(2, n + 1):
            # NOTE: We don't want to break up "simpler" ints any further.
            dp[t] = 0 if t == n else t
            for i in range(1, t):
                if t - i >= 1:
                    dp[t] = max(dp[t], dp[i] * dp[t - i])

        return dp[n]


def test() -> None:
    sol = Solution()
    print(sol.integerBreak(4))
    sol = Solution()
    print(sol.integerBreak(12))


if __name__ == "__main__":
    test()

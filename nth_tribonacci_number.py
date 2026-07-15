class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = (
            self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        )
        return self.memo[n]


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        dp.extend([0] * 35)

        if n < 3:
            # NOTE: n = 0, 1, or 2 are bases.
            return dp[n]

        for j in range(3, n + 1):
            dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

        return dp[n]


class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c

        # NOTE: n >= 3 at this point.
        # Let k represent the number of iterations required.
        k = n - 2

        while k > 0:
            temp = c
            c = a + b + c
            a = b
            b = temp
            k -= 1

        return c

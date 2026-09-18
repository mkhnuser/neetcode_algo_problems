class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 1
        if n == 1:
            return 1

        return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # NOTE: n >= 2 at this point.
        a = 1
        b = 1

        for _ in range(n - 1):
            a, b = b, a + b

        return b

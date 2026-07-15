class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            # NOTE:
            # There is 1 way to reach the step number zero.
            # There is 1 way to reach the step number one.
            return 1

        if n in self.memo:
            return self.memo[n]

        num_of_ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = num_of_ways
        return num_of_ways


class Solution:
    def __init__(self) -> None:
        # NOTE: n is between 1 and 45.
        self.memo = [None] * 46
        # NOTE: So, indecies are 0 .. 45.

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            # NOTE:
            # There is 1 way to reach the step number zero.
            # There is 1 way to reach the step number one.
            return 1

        # NOTE: n >= 2 and n <= 45 at this point.
        if self.memo[n] is not None:
            return self.memo[n]

        num_of_ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = num_of_ways
        return num_of_ways


class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        if n <= 1:
            return 1

        # NOTE: n >= 2 and n <= 45 at this point.

        k = n - 1
        for _ in range(k):
            a, b = b, a + b

        return b

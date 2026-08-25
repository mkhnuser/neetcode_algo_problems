class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        # NOTE: x != 0.

        if n == 0:
            return 1

        elif n > 0:
            res = 1
            for _ in range(n):
                res = res * x
            return res
        else:
            # NOTE: n < 0.
            m = -n
            res = 1
            for _ in range(m):
                res = res * x
            return 1 / res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def h(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = h(x * x, n // 2)
            return x * res if n % 2 else res

        res = h(x, abs(n))
        return res if n >= 0 else 1 / res


def test() -> None:
    sol = Solution()
    print(sol.myPow(2, 5))


if __name__ == "__main__":
    test()

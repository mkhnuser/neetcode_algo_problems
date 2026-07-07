class Solution:
    def isHappy(self, n: int) -> bool:
        # NOTE: n >= 1.
        seen = set()
        while n != 1:
            n = self.replace_n(n)
            if n in seen:
                return False
            seen.add(n)

        # NOTE: At this point, the number is 1, so it's a non-cyclical number.
        return True

    def replace_n(self, n: int) -> int:
        summation = 0
        while n != 0:
            n, r = divmod(n, 10)
            summation += r**2
        return summation


def test() -> None:
    sol = Solution()
    print(sol.replace_n(127))
    print(sol.replace_n(7))
    print(sol.replace_n(11))

    print(sol.isHappy(100))
    print(sol.isHappy(101))
    print(sol.isHappy(19))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(L, R):
            if L > R:
                return 0
            if (L, R) in dp:
                return dp[(L, R)]

            even = (R - L) % 2 == 0
            left = piles[L] if even else 0
            right = piles[R] if even else 0
            dp[(L, R)] = max(dfs(L + 1, R) + left, dfs(L, R - 1) + right)
            return dp[(L, R)]

        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > total - alice_score


def test() -> None:
    sol = Solution()
    print(sol.stoneGame([1, 2, 3, 1]))

    sol = Solution()
    print(sol.stoneGame([2, 1]))


if __name__ == "__main__":
    test()

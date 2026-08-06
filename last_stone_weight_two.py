from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum + 1) // 2
        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        return dfs(0, 0)


def test() -> None:
    sol = Solution()
    print(sol.lastStoneWeightII(stones=[2, 4, 1, 5, 6, 3]))
    sol = Solution()
    print(sol.lastStoneWeightII(stones=[4, 4, 1, 7, 10]))


if __name__ == "__main__":
    test()

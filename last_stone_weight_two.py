from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summation = sum(stones)
        half_summation = summation // 2
        cache = {}
        i = 0
        return self.recurse(stones, cache, i, 0, half_summation, summation)

    def recurse(
        self,
        stones: List[int],
        cache: dict,
        i: int,
        c: int,
        half_summation: int,
        summation: int,
    ) -> int:
        if i >= len(stones) or c >= half_summation:
            return abs(c - (summation - c))

        if (i, c) in cache:
            return cache[(i, c)]

        s = stones[i]

        inclusion_path = self.recurse(
            stones,
            cache,
            i + 1,
            c + s,
            half_summation,
            summation,
        )
        exclusion_path = self.recurse(
            stones,
            cache,
            i + 1,
            c,
            half_summation,
            summation,
        )
        cache[(i, c)] = min(inclusion_path, exclusion_path)
        return cache[(i, c)]


def test() -> None:
    sol = Solution()
    print(sol.lastStoneWeightII(stones=[2, 4, 1, 5, 6, 3]))
    sol = Solution()
    print(sol.lastStoneWeightII(stones=[4, 4, 1, 7, 10]))


if __name__ == "__main__":
    test()

import math
from typing import List


class Solution:
    # WARNING: This solution times out, use math.ceil for piles.
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # NOTE: h is un upper bound on the number of iterations.
        # NOTE: Try to do binary search on the rate of eating k.
        L = 1
        R = max(piles)
        output = R

        while L <= R:
            k = (L + R) // 2

            if self.can_be_eaten(piles, h, k):
                output = k
                R = k - 1
            else:
                L = k + 1

        return output

    def can_be_eaten(self, piles: List[int], h: int, k: int) -> bool:
        t = 0

        for pile in piles:
            while pile > 0:
                pile -= k
                t += 1

        return t <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # NOTE: h is un upper bound on the number of iterations.
        # NOTE: Try to do binary search on the rate of eating k.
        L = 1
        R = max(piles)
        output = R

        while L <= R:
            k = (L + R) // 2

            if self.can_be_eaten(piles, h, k):
                output = k
                R = k - 1
            else:
                L = k + 1

        return output

    def can_be_eaten(self, piles: List[int], h: int, k: int) -> bool:
        t = 0

        for pile in piles:
            t += math.ceil(pile / k)

        return t <= h

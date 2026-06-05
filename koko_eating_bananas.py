import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1

        while True:
            hours_spent = 0

            for pile in piles:
                hours_spent += math.ceil(pile / speed)

            if hours_spent <= h:
                return speed

            speed += 1


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower_bound = 1
        upper_bound = max(piles)
        output = lower_bound

        while lower_bound <= upper_bound:
            k = (lower_bound + upper_bound) // 2
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / k)
            if hours_spent <= h:
                output = k
                upper_bound = k - 1
            else:
                lower_bound = k + 1

        return output

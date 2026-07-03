from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # NOTE: days is precise number of days we have to perform loading.
        L = max(weights)
        R = sum(weights)
        res = R

        while L <= R:
            middle = (L + R) // 2
            i = 0

            for _ in range(1, days + 1):
                c = middle
                while i < len(weights) and c - weights[i] >= 0:
                    c -= weights[i]
                    i += 1

            if i >= len(weights):
                # NOTE: We've been able to load all the goods, try to decrease our capacity.
                res = middle  # NOTE: No need for min(res, middle).
                R = middle - 1
            else:
                # NOTE: i < len(weights), so some goods were not loaded, try to increase our capacity.
                L = middle + 1

        return res

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        output = [1] * n

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                output[i] = output[i - 1] + 1

        for i in range(n - 1 - 1, -1, -1):
            if ratings[i] > ratings[i + 1]:
                output[i] = max(output[i], output[i + 1] + 1)

        return sum(output)

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        p = 1
        output = []
        self.gen(n, n, k, comb, p, output)
        return output

    def gen(
        self,
        r: int,
        n: int,
        k: int,
        comb: list[int],
        p: int,
        output: list[list[int]],
    ) -> None:
        if len(comb) >= k:
            # NOTE: A combination has been obtained.
            output.append(comb.copy())
            return None

        # NOTE: The case below is redundant and is handled by the loop below it.
        # if n < k:
        #     # NOTE: We have not got enough numbers to choose from.
        #     return None

        for i in range(p, r + 1):
            comb.append(i)
            self.gen(r, n - 1, k, comb, i + 1, output)
            comb.pop()

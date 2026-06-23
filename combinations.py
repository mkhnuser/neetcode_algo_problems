from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        range_ = list(range(1, n + 1))
        output = []
        index = 0
        current_comb = []
        self.gen_combs(range_, output, index, current_comb, k)
        return output

    def gen_combs(
        self,
        range_: List[int],
        output: List[List[int]],
        index: int,
        current_comb: List[int],
        k: int,
    ) -> None:
        if len(current_comb) == k:
            output.append(current_comb.copy())
            return

        if index >= len(range_):
            return

        current_comb.append(range_[index])
        self.gen_combs(range_, output, index + 1, current_comb, k)
        current_comb.pop()
        self.gen_combs(range_, output, index + 1, current_comb, k)

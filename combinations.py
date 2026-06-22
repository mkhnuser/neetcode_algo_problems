from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        range_ = list(range(1, n + 1))
        output = []
        current_comb = []
        index = 0
        self.generate_combinations(index, range_, k, current_comb, output)
        return output

    def generate_combinations(
        self,
        index: int,
        range_: List[int],
        k: int,
        current_comb: list[int],
        output: List[List[int]],
    ) -> None:
        # NOTE:
        # range_ = [1, 2, 3], k = 2.
        # Expected output: [[1, 2], [1, 3], [2, 3]].
        if len(current_comb) >= k:
            output.append(current_comb.copy())
            return

        if index >= len(range_):
            return

        current_comb.append(range_[index])
        self.generate_combinations(index + 1, range_, k, current_comb, output)
        current_comb.pop()
        self.generate_combinations(index + 1, range_, k, current_comb, output)


def test() -> None:
    sol = Solution()
    print(sol.combine(n=3, k=2))
    print(sol.combine(n=3, k=3))
    print(sol.combine(n=3, k=1))

    print(sol.combine(n=4, k=2))


if __name__ == "__main__":
    test()

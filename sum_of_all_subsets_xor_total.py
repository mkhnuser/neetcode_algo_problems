from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = self.iterate(nums)
        return self.do_xor(subsets)

    def do_xor(self, subsets: List[List[int]]) -> int:
        output = 0

        for s in subsets:
            if not s:
                continue

            summation = s[0]

            for el in s[1:]:
                summation ^= el

            output += summation

        return output

    def iterate(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            stage = []

            for subset in subsets:
                s = subset.copy()
                s.append(num)
                stage.append(s)

            subsets.extend(stage)

        return subsets


def test() -> None:
    sol = Solution()
    print(sol.subsetXORSum([2, 4]))
    print(sol.subsetXORSum([]))


if __name__ == "__main__":
    test()

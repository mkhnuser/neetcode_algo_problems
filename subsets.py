from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        self.solve_with_iteration(nums, output)
        return output

    def solve_with_iteration(self, nums: List[int], output: List[List[int]]) -> None:
        for num in nums:
            output += [subset + [num] for subset in output]

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     index = 0
    #     output = []
    #     current_subset = []
    #     self.solve_with_backtracking(index, nums, output, current_subset)
    #     return output

    def solve_with_backtracking(
        self,
        index: int,
        nums: List[int],
        output: List[List[int]],
        current_subset: List[int],
    ) -> None:
        if index >= len(nums):
            output.append(current_subset.copy())
            return

        s = current_subset.copy()
        s.append(nums[index])
        self.solve_with_backtracking(index + 1, nums, output, s)
        s.pop()
        self.solve_with_backtracking(index + 1, nums, output, s)


def test():
    nums = [1, 2]
    sol = Solution()
    print(sol.subsets(nums))
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.subsets(nums))


if __name__ == "__main__":
    test()

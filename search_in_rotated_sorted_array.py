from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:
            middle_index = (lower_bound + upper_bound) // 2
            current = nums[middle_index]

            if current == target:
                return middle_index

            # NOTE: At this point, current != target.

            if current >= nums[lower_bound]:
                # NOTE: The left part is sorted.
                if target >= nums[lower_bound] and target < current:
                    # NOTE: Examine this left part.
                    upper_bound = middle_index - 1
                else:
                    # NOTE: OK, the left part is sorted and target is not there.
                    # Examine the right part.
                    lower_bound = middle_index + 1
            else:
                # NOTE: The left part is not sorted.
                # Then you can treat the right part as sorted.
                if target > current and target <= nums[upper_bound]:
                    lower_bound = middle_index + 1
                else:
                    upper_bound = middle_index - 1

        return -1


def test():
    sol = Solution()
    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    print(sol.search(nums, target))
    nums = [3, 5, 6, 0, 1, 2]
    target = 4
    print(sol.search(nums, target))


if __name__ == "__main__":
    test()

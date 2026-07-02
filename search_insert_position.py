from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle = (L + R) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                L = middle + 1
            else:
                # NOTE: nums[middle] > target.
                R = middle - 1

        return L


def test() -> None:
    nums = [-1, 0, 2, 4, 6, 8]  # NOTE: n = 6.
    target = 5
    sol = Solution()
    print(sol.searchInsert(nums, target))

    nums = [-1, 0, 2, 4, 6, 8]
    target = 10
    sol = Solution()
    print(sol.searchInsert(nums, target))

    nums = []
    target = 10
    sol = Solution()
    print(sol.searchInsert(nums, target))

    nums = [1]
    target = 10
    sol = Solution()
    print(sol.searchInsert(nums, target))

    nums = [1, 2, 3]
    target = 0
    sol = Solution()
    print(sol.searchInsert(nums, target))


if __name__ == "__main__":
    test()

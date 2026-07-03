from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle_index = (L + R) // 2
            middle_element = nums[middle_index]
            rightmost_element = nums[R]
            leftmost_element = nums[L]

            if middle_element == target:
                return True

            if middle_element < rightmost_element:
                # NOTE: At this point, we are sure that the right part is sorted from lowest to highest.
                if middle_element < target <= rightmost_element:
                    # NOTE: Search to the right.
                    L = middle_index + 1
                else:
                    # NOTE: target <= middle_element or target > rightmost_element.
                    # Search to the left.
                    R = middle_index - 1
            elif middle_element > rightmost_element:
                # NOTE: middle_element > rightmost_element.
                # NOTE: At this point, we are sure that the left part is sorted from lowest to highest.
                if leftmost_element <= target < middle_element:
                    # NOTE: Search to the left.
                    R = middle_index - 1
                else:
                    # NOTE: target < leftmost_element or target >= middle_element.
                    # Search to the right.
                    L = middle_index + 1
            else:
                R -= 1

        return False


def test() -> None:
    nums = [3, 4, 4, 5, 6, 1, 2, 2]
    target = 1
    sol = Solution()
    print(sol.search(nums, target))

    nums = [3, 5, 6, 0, 0, 1, 2]
    target = 4
    sol = Solution()
    print(sol.search(nums, target))


if __name__ == "__main__":
    test()

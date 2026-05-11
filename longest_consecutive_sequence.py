from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # NOTE: The next element is precisely one more than the current element.
        if not nums:
            return 0

        nums = list(set(nums))
        nums = sorted(nums)
        global_max = float("-inf")
        current = 1

        for i in range(1, len(nums)):
            current_num = nums[i]
            prev_num = nums[i - 1]
            if current_num - prev_num == 1:
                current += 1
            else:
                global_max = max(global_max, current)
                current = 1

        # NOTE: Just in case if the else block has not been hit.
        # nums = [1, 2, 3], for example.
        global_max = max(global_max, current)
        current = 0

        return int(global_max)


def test():
    nums = [2, 20, 4, 10, 3, 4, 5]
    sol = Solution()
    print(sol.longestConsecutive(nums))
    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    print(sol.longestConsecutive(nums))
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(sol.longestConsecutive(nums))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # NOTE: Store num to its index.
        diffs = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in diffs:
                ans = [diffs[diff], i]
                return ans

            diffs[num] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_table = []

        for original_index, num in enumerate(nums):
            lookup_table.append((num, original_index))

        lookup_table.sort()  # NOTE: First sort by number, then by its index.
        i = 0
        j = len(nums) - 1

        while i < j:
            summation = lookup_table[i][0] + lookup_table[j][0]

            if summation == target:
                return [
                    min(lookup_table[i][1], lookup_table[j][1]),
                    max(lookup_table[i][1], lookup_table[j][1]),
                ]
            elif summation < target:
                i += 1
            else:
                j -= 1


def test():
    sol = Solution()
    print(sol.twoSum([3, 2, 3], 6))


if __name__ == "__main__":
    test()

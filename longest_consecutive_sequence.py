from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                c = 1

                while (num + c) in nums_set:
                    c += 1
                res = max(c, res)

        return res


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

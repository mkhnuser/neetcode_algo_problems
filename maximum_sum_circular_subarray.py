from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        output = nums[0]
        n = len(nums)

        for i in range(n):
            cur_sum = 0
            j = i
            counter = 0

            while counter < n:
                # NOTE: Just go the full circle.
                if cur_sum <= 0:
                    cur_sum = 0

                cur_sum += nums[j % n]
                output = max(output, cur_sum)
                j += 1
                counter += 1

        return output


def test() -> None:
    nums = [-2, 4, -5, 4, -5, 9, 4]
    sol = Solution()
    print(sol.maxSubarraySumCircular(nums))


if __name__ == "__main__":
    test()

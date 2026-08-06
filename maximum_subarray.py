from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = float("-inf")

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray = nums[i:j]
                summation = sum(subarray)
                if summation > output:
                    output = summation

        return output


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = float("-inf")
        n = len(nums)
        current_sum = 0

        for i in range(n):
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum > output:
                    output = current_sum
            current_sum = 0

        return output


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum <= 0:
                cur_sum = 0

            cur_sum += n
            output = max(output, cur_sum)

        return output


def test() -> None:
    sol = Solution()
    print(sol.maxSubArray([-1]))
    sol = Solution()
    print(sol.maxSubArray(nums=[2, -3, 4, -2, 2, 1, -1, 4]))


if __name__ == "__main__":
    test()

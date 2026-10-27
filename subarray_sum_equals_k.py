from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur_sum = 0
        prefix_sums = {0: 1}

        for num in nums:
            cur_sum += num
            diff = cur_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

        return res


def test() -> None:
    sol = Solution()
    print(sol.subarraySum([2, -1, 1, 2], 2))


if __name__ == "__main__":
    test()

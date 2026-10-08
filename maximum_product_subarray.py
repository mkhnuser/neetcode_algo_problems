from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_, max_ = 1, 1

        for n in nums:
            tmp_max = max_ * n
            max_ = max(n * max_, n * min_, n)
            min_ = min(tmp_max, n * min_, n)
            res = max(res, max_)

        return res


def test() -> None:
    sol = Solution()
    print(sol.maxProduct([2, 4, -3, 5]))

    sol = Solution()
    print(sol.maxProduct([-3, 0, -2]))


if __name__ == "__main__":
    test()

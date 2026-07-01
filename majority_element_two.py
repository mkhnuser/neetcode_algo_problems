from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        threshold = len(nums) // 3
        res = set()
        i = 0

        while i < n:
            j = i + 1

            while j < n and nums[i] == nums[j]:
                j += 1

            count = j - i

            if count > threshold:
                res.add(nums[i])

            i = j

        return list(res)


def test() -> None:
    sol = Solution()
    print(sol.majorityElement([1, 2, 3]))


if __name__ == "__main__":
    test()

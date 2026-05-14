# TODO: Investigate the concept of a fixed-sized sliding window.
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(i + 1 + k, len(nums))):
                # NOTE: At this point, abs(i - j) <= k.
                if nums[i] == nums[j]:
                    return True
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        R = L + k
        n = len(nums)

        set_ = set()

        # NOTE: Populate a fixed-sized sliding window.
        for i in range(L, R + 1):
            if i >= n:
                continue

            num = nums[i]

            if num in set_:
                return True

            set_.add(num)

        while R < n - 1:
            L += 1
            R += 1
            set_.remove(nums[L - 1])
            candidate = nums[R]

            if candidate in set_:
                return True

            set_.add(nums[R])

        return False


def test():
    nums = [1, 2, 3, 1]
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))

    nums = [0, 99, 1, 2, 3, 1, 55, 44]
    #       0   1  2  3  4  5   6   7.
    #           L        R.
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))

    nums = [2, 1, 2]
    k = 1
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))


if __name__ == "__main__":
    test()

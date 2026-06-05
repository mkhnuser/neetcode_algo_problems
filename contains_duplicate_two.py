from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(i - j) > k:
                    continue
                if nums[i] == nums[j]:
                    return True
        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        L = 0

        for R in range(len(nums)):
            if abs(R - L) > k:
                seen.remove(nums[L])
                L += 1

            el = nums[R]

            if el in seen:
                return True

            seen.add(el)

        return False


def test():
    nums = [1, 2, 3, 1]
    #       0  1  2  3.
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))

    nums = [0, 99, 1, 2, 3, 1, 55, 44]
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))

    nums = [2, 1, 2]
    k = 1
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))


if __name__ == "__main__":
    test()

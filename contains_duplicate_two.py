from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[j] == nums[i]:
                    return True

        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L = 0
        seen = set()

        for R in range(len(nums)):
            if abs(R - L) > k:
                seen.remove(nums[L])
                L += 1

            item = nums[R]
            if item in seen:
                return True
            seen.add(item)

        return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i in range(len(nums)):
            if nums[i] in mapping and i - mapping[nums[i]] <= k:
                return True
            mapping[nums[i]] = i
        return False

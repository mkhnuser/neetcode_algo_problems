from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ = set()

        for value in nums:
            if value in set_:
                return True
            set_.add(value)

        return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

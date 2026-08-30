from typing import List


class Solution:
    def singleNumber(
        self,
        nums: List[int],
    ) -> int:
        set_ = set()

        for num in nums:
            if num in set_:
                set_.remove(num)
            else:
                set_.add(num)

        return list(set_)[0]

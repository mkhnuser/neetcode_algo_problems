from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_be_split(largest_sum):
            subarray_size = 1
            current_sum = 0

            for num in nums:
                current_sum += num

                if current_sum > largest_sum:
                    subarray_size += 1
                    if subarray_size > k:
                        return False
                    current_sum = num

            return True

        L, R = max(nums), sum(nums)
        res = R

        while L <= R:
            mid = L + (R - L) // 2

            if can_be_split(mid):
                res = mid
                R = mid - 1
            else:
                L = mid + 1

        return res

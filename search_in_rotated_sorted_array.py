from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        output = -1

        while L <= R:
            M = (L + R) // 2
            m_element = nums[M]

            if m_element == target:
                return M

            leftmost_element = nums[L]
            rightmost_element = nums[R]

            if m_element >= leftmost_element:
                # NOTE: Left part is sorted.
                if leftmost_element <= target < m_element:
                    R = M - 1
                else:
                    L = M + 1
            else:
                # NOTE: Right part is sorted.
                if m_element < target <= rightmost_element:
                    L = M + 1
                else:
                    R = M - 1

        return output

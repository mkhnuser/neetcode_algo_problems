from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        combined_length = len(nums1) + len(nums2)
        half_combined_length = combined_length // 2

        if len(B) < len(A):
            A, B = B, A

        L, R = 0, len(A) - 1

        while True:
            i = (L + R) // 2
            j = half_combined_length - i - 2

            A_left_el = A[i] if i >= 0 else float("-infinity")
            A_right_el = A[i + 1] if (i + 1) < len(A) else float("infinity")
            B_left_el = B[j] if j >= 0 else float("-infinity")
            B_right_el = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if A_left_el <= B_right_el and B_left_el <= A_right_el:
                if combined_length % 2:
                    return min(A_right_el, B_right_el)
                return (max(A_left_el, B_left_el) + min(A_right_el, B_right_el)) / 2
            elif A_left_el > B_right_el:
                R = i - 1
            else:
                L = i + 1

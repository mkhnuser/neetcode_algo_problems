from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        L = 0
        R = 0

        while R < n:
            if nums1[L] > nums2[R]:
                self.shift_right(nums1, start_index=L)
                nums1[L] = nums2[R]
                L += 1
                R += 1

            elif nums1[L] <= nums2[R]:
                if L >= m and nums1[L] == 0:
                    # NOTE: Populate zeroes.
                    nums1[L] = nums2[R]
                    R += 1
                L += 1

    def shift_right(self, arr: List[int], start_index: int) -> None:
        prev_erased = None

        for i in range(start_index, len(arr) - 1):
            if prev_erased is None:
                prev_erased = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = 0
            else:
                to_be_erased = arr[i + 1]
                arr[i + 1] = prev_erased
                prev_erased = to_be_erased


def test():
    sol = Solution()
    test = ["a", "b", "c", 0, 0]
    sol.shift_right(test, 0)
    print(test)
    sol.shift_right(test, 0)
    print(test)


if __name__ == "__main__":
    test()

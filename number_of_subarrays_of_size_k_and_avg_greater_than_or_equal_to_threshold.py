from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        counter = 0

        for i in range(n):
            if n - i < k:
                # NOTE: The subarrays have to be precisely of length k.
                continue
            summation = arr[i]
            for j in range(i + 1, min(i + k, n)):
                summation += arr[j]
            avg = summation / k
            if avg >= threshold:
                counter += 1

        return counter


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        counter = 0

        for L in range(n):
            R = min((L + k) - 1, n - 1)
            if (R - L) + 1 < k:
                continue

            # NOTE: At this point, window = [L, R] is of size 3.
            summation = sum(arr[L : R + 1])
            avg = summation / k
            if avg >= threshold:
                counter += 1

        return counter


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        counter = 0
        summation = 0

        # NOTE: 1. Initialize a window.
        # 2. Run the window.

        for i in range(0, k):
            if i >= n:
                # NOTE: An input array may be of size 1 or 2.
                break
            summation += arr[i]

        avg = summation / k
        if avg >= threshold:
            counter += 1

        if n <= k:
            return counter

        # NOTE: At this point, the first window iteration has been done.

        for L in range(1, n):
            R = (L + k) - 1

            if R >= n:
                break

            summation -= arr[L - 1]
            summation += arr[R]
            avg = summation / k

            if avg >= threshold:
                counter += 1

        return counter


def test():
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    #      0  1  2  3  4  5  6  7.    n = 8.
    #                        L  R
    k = 3
    threshold = 4
    sol = Solution()
    print(sol.numOfSubarrays(arr, k, threshold))

    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k = 3
    threshold = 5
    sol = Solution()
    print(sol.numOfSubarrays(arr, k, threshold))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 2
    threshold = 5
    sol = Solution()
    print(sol.numOfSubarrays(arr, k, threshold))


if __name__ == "__main__":
    test()

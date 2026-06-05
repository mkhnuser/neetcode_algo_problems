from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                arr_size = (j - i) + 1
                if arr_size != k:
                    continue
                summation = sum(arr[i : j + 1])
                avg = summation / k
                if avg >= threshold:
                    counter += 1

        return counter


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0

        for i in range(len(arr)):
            R = min(len(arr) - 1, i + k - 1)
            arr_size = (R - i) + 1
            if arr_size != k:
                continue
            summation = sum(arr[i : R + 1])
            avg = summation / k
            if avg >= threshold:
                counter += 1

        return counter


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0

        L = 0
        summation = 0
        for R in range(len(arr)):
            arr_size = (R - L) + 1

            if arr_size > k:
                summation -= arr[L]
                L += 1

            summation += arr[R]

            arr_size = (R - L) + 1

            if arr_size < k:
                continue

            avg = summation / k
            if avg >= threshold:
                counter += 1

        return counter


def test():
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    #      0  1  2  3  4  5  6  7.    n = 8.
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

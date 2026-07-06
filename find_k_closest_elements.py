import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = float("+inf")
        closest_index = None
        seen_indecies = set()
        output = []

        for _ in range(k):
            for i in range(len(arr)):
                num = arr[i]
                if i not in seen_indecies and abs(num - x) < abs(x - closest):
                    closest = num
                    closest_index = i

            output.append(closest)
            seen_indecies.add(closest_index)
            closest = float("+inf")

        output.sort()
        return output


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []

        for num in arr:
            tuple_ = (abs(x - num), num)
            heapq.heappush(min_heap, tuple_)

        output = [heapq.heappop(min_heap)[-1] for _ in range(k)]
        output.sort()
        return output


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num: (abs(x - num), num))
        return sorted(arr[:k])


def test() -> None:
    arr = [2, 4, 5, 8]
    k = 2
    x = 6
    sol = Solution()
    print(sol.findClosestElements(arr, k, x))

    arr = [2, 3, 4]
    k = 3
    x = 1
    sol = Solution()
    print(sol.findClosestElements(arr, k, x))


if __name__ == "__main__":
    test()

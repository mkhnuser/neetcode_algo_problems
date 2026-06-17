import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self.shrink()

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self.shrink()
        return self.nums[0]

    def shrink(self) -> None:
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

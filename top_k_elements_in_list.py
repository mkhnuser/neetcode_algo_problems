from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        sorted_by_count = sorted(freq_map.items(), key=lambda item: item[-1])
        return [item[0] for item in sorted_by_count[-k:]]


def test():
    sol = Solution()
    print(sol.topKFrequent([1, 2, 2, 3, 3, 3], 2))
    print(sol.topKFrequent([7, 7], 2))


if __name__ == "__main__":
    test()

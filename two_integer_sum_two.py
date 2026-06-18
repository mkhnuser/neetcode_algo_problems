from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1
            else:
                return [i + 1, j + 1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                m = (l + r) // 2
                if numbers[m] + numbers[i] == target:
                    return [i + 1, m + 1]
                elif numbers[m] + numbers[i] > target:
                    r = m - 1
                else:
                    l = m + 1

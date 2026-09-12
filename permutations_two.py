from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        mapping = {}

        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1

        output = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                output.append(perm.copy())
                return None

            for n in mapping:
                if mapping[n] > 0:
                    perm.append(n)
                    mapping[n] -= 1
                    dfs()
                    mapping[n] += 1
                    perm.pop()

        dfs()
        return output

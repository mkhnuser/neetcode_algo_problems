from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # NOTE: [1, 2, 3].
        # 1 -> permute [2, 3].
        # 2 -> permute [1, 3].
        # 3 -> permute [1, 2].

        output = []
        self.recurse(nums, [], output, len(nums))
        return output

    def recurse(
        self,
        nums: List[int],
        perm: List[int],
        output: List[List[int]],
        n: int,
    ) -> None:
        for i in range(len(nums)):
            current_num = nums[i]
            perm.append(current_num)
            the_rest = nums[:i] + nums[i + 1 :]
            self.recurse(the_rest, perm, output, n)
            perm.pop()

        if len(perm) == n:
            output.append(perm.copy())


# NOTE: An optimized version, don't create a new array every time.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # NOTE: [1, 2, 3].
        # 1 -> permute [2, 3].
        # 2 -> permute [1, 3].
        # 3 -> permute [1, 2].

        output = []
        n = len(nums)
        self.recurse(nums, [], [False] * n, n, output)
        return output

    def recurse(
        self,
        nums: List[int],
        perm: List[int],
        was_picked: List[int],
        n: int,
        output: List[List[int]],
    ) -> None:
        if len(perm) == n:
            output.append(perm.copy())
            return None

        for i in range(n):
            if not was_picked[i]:
                current_num = nums[i]
                was_picked[i] = True
                perm.append(current_num)

                self.recurse(nums, perm, was_picked, n, output)

                perm.pop()
                was_picked[i] = False


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.iterate(nums)

    def iterate(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        # NOTE: An approach similar to generating all subsets is used.
        # NOTE: perms = [[]]
        # NOTE: perms = [[1]]
        # NOTE: perms = [[1, 2], [2, 1]]
        # NOTE: perms = [[3, 1, 2], [1, 3, 2], [1, 2, 3], [3, 2, 1], [2, 3, 1], [2, 1, 3]]

        for num in nums:
            stage = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, num)
                    stage.append(perm_copy)

            perms = stage

        return perms

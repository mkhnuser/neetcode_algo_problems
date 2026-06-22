from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # output = []
        # current_perm = []
        # self.recurse_permutations(nums, current_perm, output, n=len(nums))
        # return output
        return self.iterate_permutations(nums)

    def iterate_permutations(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for j in range(len(p) + 1):
                    new_p = p.copy()
                    new_p.insert(j, n)
                    new_perms.append(new_p)

            perms = new_perms
        return perms

    def recurse_permutations(
        self,
        nums: List[int],
        current_perm: List[int],
        output: List[List[int]],
        n,
    ) -> None:
        for i in range(len(nums)):
            current_perm.append(nums[i])
            # NOTE: Make perms for all nums except the current one.
            new_nums = nums[0:i] + nums[i + 1 :]
            self.recurse_permutations(new_nums, current_perm, output, n)
            current_perm.pop()

        if len(current_perm) == n:
            output.append(current_perm.copy())


def test():
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    print(sol.permute([1]))
    print(sol.permute([1, 2]))
    print(sol.permute([1, 2, 3, 4]))


if __name__ == "__main__":
    test()

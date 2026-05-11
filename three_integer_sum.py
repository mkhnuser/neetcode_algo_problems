from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # NOTE: O(n ** 3) in terms of time.
        # Bad, bad, bad.
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if i == j or i == k or j == k:
                        continue

                    num_one = nums[i]
                    num_two = nums[j]
                    num_three = nums[k]
                    summation = num_one + num_two + num_three

                    if summation == 0:
                        triplet = [num_one, num_two, num_three]
                        triplet.sort()
                        triplet = tuple(triplet)
                        res.add(triplet)

        return [list(triplet) for triplet in res]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        history = set()
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[i] + nums[j]
                target = -diff
                if target in history:
                    t = [target, nums[i], nums[j]]
                    res.add(tuple(t))
            history.add(nums[i])

        return [list(t) for t in res]


def test():
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))
    nums = [0, 1, 1]
    print(sol.threeSum(nums))
    nums = [0, 0, 0]
    print(sol.threeSum(nums))


if __name__ == "__main__":
    test()

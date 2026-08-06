from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        subset_indecies = set()
        self.gen_all_subset_indecies(len(nums), nums, subset_indecies, 0, [])

        for subset1_indecies in subset_indecies:
            subset1_indecies = set(subset1_indecies)
            subset2_indecies = set(range(len(nums))) - subset1_indecies
            subset1_sum = sum(
                num for i, num in enumerate(nums) if i in subset1_indecies
            )
            subset2_sum = sum(
                num for i, num in enumerate(nums) if i in subset2_indecies
            )
            if subset1_sum == subset2_sum:
                return True

        return False

    def gen_all_subset_indecies(
        self,
        n: int,
        nums: list[int],
        subset_indecies: set[tuple],
        current_index: int,
        index_seq: list[int],
    ) -> None:
        if current_index >= n:
            subset_indecies.add(tuple(index_seq))
            return

        index_seq.append(current_index)
        self.gen_all_subset_indecies(
            n,
            nums,
            subset_indecies,
            current_index + 1,
            index_seq,
        )
        index_seq.pop()
        self.gen_all_subset_indecies(
            n,
            nums,
            subset_indecies,
            current_index + 1,
            index_seq,
        )


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        indecies = self.gen_all_subset_indecies(nums)

        for subset1_indecies in indecies:
            subset1_indecies = set(subset1_indecies)
            subset2_indecies = set(range(len(nums))) - subset1_indecies
            subset1_sum = sum(
                num for i, num in enumerate(nums) if i in subset1_indecies
            )
            subset2_sum = sum(
                num for i, num in enumerate(nums) if i in subset2_indecies
            )
            if subset1_sum == subset2_sum:
                return True

        return False

    def gen_all_subset_indecies(self, nums: list[int]) -> list[list]:
        output = [[]]
        for i, num in enumerate(nums):
            stage = []
            for s in output:
                new_s = s.copy()
                new_s.append(i)
                stage.append(new_s)
            output.extend(stage)
        return output


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # NOTE: X + X = 2X = summation.
        # Therefore, X = summation / 2.
        # Moreover, X must be an integer, since all values of nums are ints.
        summation = sum(nums)
        if summation % 2:
            return False

        n = len(nums)
        half_summation = summation / 2

        def dfs(i: int, target: int, cache: dict) -> bool:
            if i >= n:
                return target == 0
            if target < 0:
                return False

            if (i, target) in cache:
                return cache[(i, target)]

            path_with_excluded_num = dfs(i + 1, target, cache)
            path_with_included_num = dfs(i + 1, target - nums[i], cache)
            cache[(i, target)] = path_with_excluded_num or path_with_included_num
            return cache[(i, target)]

        return dfs(0, half_summation, {})


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # NOTE: X + X = 2X = summation.
        # Therefore, X = summation / 2.
        # Moreover, X must be an integer, since all values of nums are ints.
        summation = sum(nums)

        if summation % 2:
            return False

        n = len(nums)
        half_summation = summation / 2
        event_horizon = set([0])

        for n in nums:
            replica = event_horizon.copy()
            for e in event_horizon:
                replica.add(e + n)
                if half_summation in replica:
                    return True
            event_horizon = replica

        return False


def test() -> None:
    sol = Solution()
    print(sol.canPartition([1, 2, 3, 4]))
    sol = Solution()
    print(sol.canPartition([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    test()

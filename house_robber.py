from typing import List, MutableMapping


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: At every position i, you can either rob a house or not to rob a house.
        return self.dfs(nums, 0, 0, 0)

    def dfs(
        self,
        nums: List[int],
        i: int,
        current_profit: int,
        max_profit: int,
    ) -> int:
        if i >= len(nums):
            return max_profit

        current_house_profit = nums[i]

        # NOTE: Rob the current house recursion branch.
        robbing_path = self.dfs(
            nums,
            i + 2,
            current_profit + current_house_profit,
            max(max_profit, current_profit + current_house_profit),
        )

        # NOTE: Don't rob.
        non_robbing_path = self.dfs(
            nums,
            i + 1,
            current_profit,
            max(max_profit, current_profit),
        )

        return max(robbing_path, non_robbing_path)


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: At every position i, you can either rob a house or not to rob a house.
        # NOTE: Let's also cache the max profit one can obtain starting from ith position.
        return self.dfs(nums, 0, 0, 0, {})

    def dfs(
        self,
        nums: List[int],
        i: int,
        current_profit: int,
        max_profit: int,
        cache: MutableMapping[tuple, int],
    ) -> int:
        if i >= len(nums):
            return max_profit

        if (i, current_profit, max_profit) in cache:
            return cache[(i, current_profit, max_profit)]

        current_house_profit = nums[i]

        # NOTE: Rob the current house recursion branch.
        robbing_path = self.dfs(
            nums,
            i + 2,
            current_profit + current_house_profit,
            max(max_profit, current_profit + current_house_profit),
            cache,
        )

        # NOTE: Don't rob.
        non_robbing_path = self.dfs(
            nums,
            i + 1,
            current_profit,
            max(max_profit, current_profit),
            cache,
        )

        cache[(i, current_profit, max_profit)] = max(
            robbing_path, non_robbing_path, max_profit
        )
        return cache[(i, current_profit, max_profit)]


# NOTE: Let's try to get rid of an accumulated profit to greatly simplify the code.


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: At every position i, you can either rob a house or not to rob a house.
        return self.dfs(nums, 0)

    def dfs(
        self,
        nums: List[int],
        i: int,
    ) -> int:
        if i >= len(nums):
            return 0

        robbing_path = self.dfs(nums, i + 2)
        non_robbing_path = self.dfs(nums, i + 1)
        return max(nums[i] + robbing_path, non_robbing_path)


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: At every position i, you can either rob a house or not to rob a house.
        return self.dfs(nums, 0, {})

    def dfs(
        self,
        nums: List[int],
        i: int,
        cache: MutableMapping[int, int],
    ) -> int:
        if i >= len(nums):
            return 0

        if i in cache:
            return cache[i]

        robbing_path = self.dfs(nums, i + 2, cache)
        non_robbing_path = self.dfs(nums, i + 1, cache)
        cache[i] = max(nums[i] + robbing_path, non_robbing_path)
        return cache[i]


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: At every position i, you can either rob a house or not to rob a house.
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # NOTE: len(nums) >= 2 at this point.

        # NOTE:
        # Let dp[i] answer this quesiton: what's the maximum profit that can be obtained up to ith position?
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(dp)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        # NOTE: At every position i, you can either rob a house or not to rob a house.
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # NOTE: len(nums) >= 2 at this point.

        # NOTE:
        # a = max profit up until prev house.
        # b = max profit up until current house.
        a = nums[0]
        b = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(nums[i] + a, b)

        return b


def test() -> None:
    nums = [1, 1, 3, 3]
    sol = Solution()
    print(sol.rob(nums))

    nums = [2, 9, 8, 3, 6]
    sol = Solution()
    print(sol.rob(nums))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        visited_set = set()

        def dfs(i):
            if i in visited_set:
                return False

            visited_set.add(i)

            if i == len(nums) - 1:
                return True
            if i > len(nums):
                return False

            jump_size = nums[i]
            # NOTE:
            # Suppose:
            # i = 2, jump_size = 2.
            # j = 3, 4.
            for j in range(i + 1, i + jump_size + 1):
                if dfs(j):
                    return True
            return False

        return dfs(i)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True
        # NOTE: The question we ask: dp[i] <=> can we reach the index n - 1 from i?

        for i in range(len(dp) - 2, -1, -1):
            jump_length = nums[i]

            if i + jump_length >= len(nums) - 1:
                dp[i] = True
                continue

            # NOTE: At this point, i + jump_length < len(nums) - 1.
            for j in range(i + 1, i + jump_length + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]


def test() -> None:
    nums = [1, 2, 0, 1, 0]
    sol = Solution()
    print(sol.canJump(nums))


if __name__ == "__main__":
    test()

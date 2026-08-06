from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # NOTE: Find the largest subset with at most m zeroes and n ones.
        length = len(strs)

        def dfs(i: int, current_subset: list[str], cache: dict) -> int:
            if i >= length:
                zero_counter = 0
                one_counter = 0
                for string in current_subset:
                    for el in string:
                        if el == "0":
                            zero_counter += 1
                        else:
                            one_counter += 1

                if zero_counter <= m and one_counter <= n:
                    return len(current_subset)
                return 0

            if (i, tuple(current_subset)) in cache:
                return cache[(i, tuple(current_subset))]

            current_string = strs[i]
            current_subset.append(current_string)
            inclusive_path = dfs(i + 1, current_subset, cache)
            current_subset.pop()
            exclusive_path = dfs(i + 1, current_subset, cache)

            cache[(i, tuple(current_subset))] = max(inclusive_path, exclusive_path)
            return cache[(i, tuple(current_subset))]

        return dfs(0, [], {})


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # NOTE: Find the largest subset with at most m zeroes and n ones.
        length = len(strs)

        def dfs(i: int, current_subset: list[str], cache: dict) -> int:
            if i >= length:
                return len(current_subset)

            if (i, tuple(current_subset)) in cache:
                return cache[(i, tuple(current_subset))]

            current_string = strs[i]
            current_subset.append(current_string)

            zero_counter = 0
            one_counter = 0
            for string in current_subset:
                for el in string:
                    if el == "0":
                        zero_counter += 1
                    else:
                        one_counter += 1

            inclusive_path = 0
            if zero_counter <= m and one_counter <= n:
                inclusive_path = dfs(i + 1, current_subset, cache)

            current_subset.pop()
            exclusive_path = dfs(i + 1, current_subset, cache)

            cache[(i, tuple(current_subset))] = max(inclusive_path, exclusive_path)
            return cache[(i, tuple(current_subset))]

        return dfs(0, [], {})


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # NOTE: For each string, how many zeroes and ones are there?

        arr = [[0] * 2 for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                arr[i][ord(c) - ord("0")] += 1

        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if m == 0 and n == 0:
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]

            # NOTE: Exclusion path.
            res = dfs(i + 1, m, n)

            if m >= arr[i][0] and n >= arr[i][1]:
                # NOTE: Inclusion path.
                res = max(res, 1 + dfs(i + 1, m - arr[i][0], n - arr[i][1]))

            dp[(i, m, n)] = res
            return res

        return dfs(0, m, n)


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # NOTE: How many zeroes and ones are there in each string?
        arr = [[0] * 2 for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                arr[i][ord(c) - ord("0")] += 1

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        # NOTE: dp[i][j][k] <=>
        # What's the largest subset that can be obtained
        # For all strings up to <i>
        # With at most <j> zeroes and <k> ones?

        for i in range(1, len(strs) + 1):
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= arr[i - 1][0] and k >= arr[i - 1][1]:
                        dp[i][j][k] = max(
                            dp[i][j][k],
                            1 + dp[i - 1][j - arr[i - 1][0]][k - arr[i - 1][1]],
                        )

        return dp[len(strs)][m][n]


def test() -> None:
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    sol = Solution()
    print(sol.findMaxForm(strs, m, n))

    strs = ["10", "0", "1"]
    m = 1
    n = 1
    sol = Solution()
    print(sol.findMaxForm(strs, m, n))


if __name__ == "__main__":
    test()

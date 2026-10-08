class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}
        i = 0
        return self.recurse(s, dp, i)

    def recurse(self, s: str, dp: dict, i: int) -> int:
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0

        ways = 0
        just_skip_current_digit_path = self.recurse(s, dp, i + 1)
        ways += just_skip_current_digit_path

        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
            skip_next_digit_path = self.recurse(s, dp, i + 2)
            ways += skip_next_digit_path

        dp[i] = ways
        return dp[i]


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]

        return dp[0]

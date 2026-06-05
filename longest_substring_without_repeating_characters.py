class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                char = s[j]
                if char in seen:
                    break
                seen.add(char)

            max_len = max(max_len, len(seen))

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        max_len = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            seen.add(s[R])
            max_len = max(max_len, R - L + 1)
        return max_len


def test():
    s = "zxyzxyz"
    #    0123456
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # 3

    s = "xxxx"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # 1

    s = "x"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # 1

    s = ""
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # 0

    s = "au"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # 2

    s = "dvdf"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))  # 3


if __name__ == "__main__":
    test()

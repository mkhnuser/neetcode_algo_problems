from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        min_s = min(strs, key=len)

        for i in range(len(min_s)):
            for s in strs:
                if s[i] != min_s[i]:
                    return output

            output += min_s[i]

        return output


def test():
    sol = Solution()
    strs = ["bat", "bag", "bank", "band"]
    print(sol.longestCommonPrefix(strs))
    strs = ["dance", "dag", "danger", "damage"]
    print(sol.longestCommonPrefix(strs))
    strs = ["neet", "feet"]
    print(sol.longestCommonPrefix(strs))
    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))


if __name__ == "__main__":
    test()

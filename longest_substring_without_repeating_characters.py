class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        output = 0

        for R in range(len(s)):
            char = s[R]

            while char in seen:
                seen.remove(s[L])
                L += 1

            seen.add(char)
            output = max(output, R - L + 1)

        return output


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        mapping = {}
        L = 0

        for R in range(len(s)):
            if s[R] in mapping:
                # NOTE: Jump to the correct position immediately.
                L = max(L, mapping[s[R]] + 1)
            mapping[s[R]] = R
            output = max(output, R - L + 1)

        return output


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break

                seen.add(s[j])
                output = max(output, j - i + 1)

        return output

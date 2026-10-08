from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        i = 0
        cache = {}
        return self.recurse(s, word_dict, cache, i)

    def recurse(self, s: str, word_dict: set[str], cache: dict, i: int) -> bool:
        if i >= len(s):
            return True
        if s[i:] in word_dict:
            return True

        if i in cache:
            return cache[i]

        for j in range(i, len(s)):
            if s[i : j + 1] not in word_dict:
                continue

            word_break_path = self.recurse(s, word_dict, cache, j + 1)
            if word_break_path:
                # NOTE: Starting from position `i`, it's in fact possible to break the word.
                cache[i] = True
                return cache[i]

        # NOTE: Starting from position `i`, it's impossible to break the word.
        cache[i] = False
        return cache[i]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_dict = wordDict
        dp = [False for _ in range(n + 1)]
        # NOTE: We can break the empty string.
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for w in word_dict:
                p = len(w)
                shift = i + p

                if shift <= n and s[i:shift] == w:
                    dp[i] = dp[shift]
                if dp[i]:
                    # NOTE: A match has occurred.
                    break

        return dp[0]


def test() -> None:
    sol = Solution()
    print(sol.wordBreak(s="neetcode", wordDict=["neet", "code"]))

    sol = Solution()
    print(sol.wordBreak(s="applepenapple", wordDict=["apple", "pen", "ape"]))

    sol = Solution()
    print(sol.wordBreak(s="catsincars", wordDict=["cats", "cat", "sin", "in", "car"]))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        allowed_words = set(wordDict)
        i = 0
        current_words = []
        self.recurse(s, i, current_words, allowed_words, output)
        return output

    def recurse(
        self,
        s: str,
        i: int,
        current_words: List[str],
        allowed_words: set[str],
        output: List[str],
    ) -> None:
        if i >= len(s):
            for word in current_words:
                if word not in allowed_words:
                    return None

            output.append(" ".join(current_words))
            return None

        for word in current_words:
            if word not in allowed_words:
                return None

        # NOTE: Starting from index i, let's try to put every possible space.
        # Once a space has been put, recurse on the remainder of the string.
        for j in range(i, len(s)):
            current_words.append(s[i : j + 1])
            self.recurse(s, j + 1, current_words, allowed_words, output)
            current_words.pop()


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        allowed_words = set(wordDict)
        i = 0
        current_words = []
        self.recurse(s, i, current_words, allowed_words, output)
        return output

    def recurse(
        self,
        s: str,
        i: int,
        current_words: List[str],
        allowed_words: set[str],
        output: List[str],
    ) -> None:
        if i >= len(s):
            output.append(" ".join(current_words))
            return None

        # NOTE: Starting from index i, let's try to put every possible space.
        # Once a space has been put, recurse on the remainder of the string.
        for j in range(i, len(s)):
            word = s[i : j + 1]

            if word not in allowed_words:
                continue

            current_words.append(word)
            self.recurse(s, j + 1, current_words, allowed_words, output)
            current_words.pop()


def test() -> None:
    s = "neetcode"
    wordDict = ["neet", "code"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))

    s = "racecariscar"
    wordDict = ["racecar", "race", "car", "is"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))

    s = "catsincars"
    wordDict = ["cats", "cat", "sin", "in", "car"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))


if __name__ == "__main__":
    test()

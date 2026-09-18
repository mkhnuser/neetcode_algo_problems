# NOTE: The first rough attempt with string modification.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a = word1
        b = word2
        # NOTE: Mold a into b.
        return self.recurse(a, b, 0, 0)

    def recurse(self, a: str, b: str, i: int, j: int) -> int:
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i

        if a[i] == b[j]:
            # NOTE: No operation is required, just proceed to next chars.
            return self.recurse(a, b, i + 1, j + 1)

        # NOTE: The two current characters are not equal.

        # NOTE: Insert b's char just before a's char.
        new_a = a[:i] + b[j] + a[i:]
        insertion_path = self.recurse(new_a, b, i + 1, j + 1)
        # NOTE: Delete a's char.
        new_a = a[:i] + a[i + 1 :]
        deletion_path = self.recurse(new_a, b, i, j)
        # NOTE: Replace a's char with b's char.
        new_a = a[:i] + b[j] + a[i + 1 :]
        replacement_path = self.recurse(new_a, b, i + 1, j + 1)
        return 1 + min(
            insertion_path,
            deletion_path,
            replacement_path,
        )


# NOTE: The second round without string modification.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a = word1
        b = word2
        # NOTE: Mold a into b.
        return self.recurse(a, b, 0, 0)

    def recurse(self, a: str, b: str, i: int, j: int) -> int:
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i

        if a[i] == b[j]:
            # NOTE: No operation is required, just proceed to next chars.
            return self.recurse(a, b, i + 1, j + 1)

        # NOTE: The two current characters are not equal.
        # At this point, we try to answer the question:
        # - What's the minimum number of operations are needed to mold a[i:] into b[j:]?

        # NOTE: Insert b's char just before a's char.
        insertion_path = self.recurse(a, b, i, j + 1)
        # NOTE: Delete a's char.
        deletion_path = self.recurse(a, b, i + 1, j)
        # NOTE: Replace a's char with b's char.
        replacement_path = self.recurse(a, b, i + 1, j + 1)
        return 1 + min(
            insertion_path,
            deletion_path,
            replacement_path,
        )


# NOTE: A top-down DP.
from typing import MutableMapping


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a = word1
        b = word2
        # NOTE: Mold a into b.
        return self.recurse(a, b, 0, 0, {})

    def recurse(
        self,
        a: str,
        b: str,
        i: int,
        j: int,
        cache: MutableMapping[tuple[int, int], int],
    ) -> int:
        if i == len(a):
            return len(b) - j
        if j == len(b):
            return len(a) - i

        if (i, j) in cache:
            return cache[(i, j)]

        if a[i] == b[j]:
            # NOTE: No operation is required, just proceed to next chars.
            cache[(i, j)] = self.recurse(a, b, i + 1, j + 1, cache)
            return cache[(i, j)]

        # NOTE: The two current characters are not equal.
        # At this point, we try to answer the question:
        # - What's the minimum number of operations are needed to mold a[i:] into b[j:]?

        # NOTE: Insert b's char just before a's char.
        insertion_path = self.recurse(a, b, i, j + 1, cache)
        # NOTE: Delete a's char.
        deletion_path = self.recurse(a, b, i + 1, j, cache)
        # NOTE: Replace a's char with b's char.
        replacement_path = self.recurse(a, b, i + 1, j + 1, cache)
        cache[(i, j)] = 1 + min(
            insertion_path,
            deletion_path,
            replacement_path,
        )
        return cache[(i, j)]


# NOTE: A bottom-up DP.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # NOTE: Mold a into b.
        a = word1
        b = word2
        n = len(a)
        m = len(b)

        # NOTE: Let dp[i][j] answer the question:
        # - What's the minimum number of operations are needed to mold a[i:] into b[j:]?
        dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

        # NOTE: "" "abc"; "" "bc"; "" "c"; "" "".
        for j in range(m):
            dp[-1][j] = m - j

        # NOTE: "abc" ""; "bc" ""; "" "c"; "" "".
        for i in range(n):
            dp[i][-1] = n - i

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


def test() -> None:
    sol = Solution()
    print(sol.minDistance(word1="monkeys", word2="money"))

    sol = Solution()
    print(sol.minDistance(word1="neatcdee", word2="neetcode"))

    sol = Solution()
    print(sol.minDistance(word1="asdf", word2="zxcv"))


if __name__ == "__main__":
    test()

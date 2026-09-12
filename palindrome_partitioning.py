from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        self.recurse(s, 0, [], output)
        return output

    def recurse(
        self,
        s: str,
        i: int,
        partition: List[str],
        output: List[List[str]],
    ) -> None:
        if i >= len(s):
            output.append(partition.copy())
            return None

        for j in range(i, len(s)):
            if self.is_palindrome(s, i, j):
                partition.append(s[i : j + 1])
                self.recurse(s, j + 1, partition, output)
                partition.pop()

    def is_palindrome(self, s: str, L: int, R: int) -> bool:
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True

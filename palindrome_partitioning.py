from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partition = []
        output = []
        self.recurse(s, 0, partition, output)
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

        # NOTE: Given an index i, consider paths from s[i] onward till the end of a string.
        for j in range(i, len(s)):
            if self.is_palindrome(s[i : j + 1]):
                partition.append(s[i : j + 1])
                self.recurse(s, j + 1, partition, output)
                partition.pop()

    def is_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

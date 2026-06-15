from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        L = 0
        R = len(s) - 1

        while L < R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1


class Solution:
    def reverseString(self, s: List[str]) -> None:
        L = 0
        R = len(s) - 1

        def reverse(L, R):
            if L < R:
                reverse(L + 1, R - 1)
                s[L], s[R] = s[R], s[L]

        reverse(L, R)


class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        for i in range(len(s)):
            s[i] = stack.pop()

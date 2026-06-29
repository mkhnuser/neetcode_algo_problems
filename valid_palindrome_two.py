class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return self.is_palindrome(s, L, R - 1) or self.is_palindrome(
                    s,
                    L + 1,
                    R,
                )

            L += 1
            R -= 1

        return True

    def is_palindrome(self, s: str, L: int, R: int) -> bool:
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True

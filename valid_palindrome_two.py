class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return is_palindrome(L + 1, R) or is_palindrome(L, R - 1)
            L += 1
            R -= 1

        return True

import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        allowed_char_range = string.ascii_letters + string.digits
        allowed_char_range = set(allowed_char_range)

        chars = []
        for char in s:
            if char in allowed_char_range:
                chars.append(char)

        s = "".join(chars)

        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1

        return True

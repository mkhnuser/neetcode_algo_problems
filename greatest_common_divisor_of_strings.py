class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_divisor(l):
            if len1 % l or len2 % l:
                return False

            f1 = len1 // l
            f2 = len2 // l

            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                return str1[:l]

        return ""

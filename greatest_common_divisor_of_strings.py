class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate = min(str1, str2, key=len)
        # NOTE: We know that a candidate divides itself.
        # So, check the largest string.
        to_be_checked = max(str1, str2, key=len)

        c = ""
        t = candidate
        # NANANA
        # NANA

        while t:
            while len(c) < len(to_be_checked):
                c += t
                if c == to_be_checked and c == candidate:
                    return t
            t = t[:-1]
            c = ""

        return t

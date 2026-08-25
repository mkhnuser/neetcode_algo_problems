class Solution:
    def romanToInt(self, s: str) -> int:
        ROMANS = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and ROMANS[s[i]] < ROMANS[s[i + 1]]:
                res -= ROMANS[s[i]]
            else:
                res += ROMANS[s[i]]

        return res

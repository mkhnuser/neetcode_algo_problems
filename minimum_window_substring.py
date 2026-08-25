class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        window = {}
        have, need = 0, len(t_count)
        res, resLen = [-1, -1], float("infinity")
        L = 0

        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = R - L + 1

                window[s[L]] -= 1
                if s[L] in t_count and window[s[L]] < t_count[s[L]]:
                    have -= 1
                L += 1

        L, R = res
        return s[L : R + 1] if resLen != float("infinity") else ""

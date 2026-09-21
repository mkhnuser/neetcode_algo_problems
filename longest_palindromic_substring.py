class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        output_len = -1
        output_left = -1
        output_right = -1

        for i in range(n):
            L = R = i
            L, R = self.get_pal_boundaries(L, R, s, n)
            current_len = R - L + 1

            if current_len > output_len:
                output_len = current_len
                output_left = L
                output_right = R

            L = R = i
            L -= 1
            L, R = self.get_pal_boundaries(L, R, s, n)
            current_len = R - L + 1

            if current_len > output_len:
                output_len = current_len
                output_left = L
                output_right = R

        return s[output_left : output_right + 1]

    def get_pal_boundaries(self, L: int, R: int, s: str, n: int) -> tuple[int, int]:
        while 0 <= L and R <= n - 1 and s[L] == s[R]:
            L -= 1
            R += 1

        return L + 1, R - 1

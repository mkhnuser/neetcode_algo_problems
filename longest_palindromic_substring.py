class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        output_len = -1
        output = None

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                is_palindrome = self.is_palindrome(substring)
                if is_palindrome and len(substring) > output_len:
                    output_len = len(substring)
                    output = substring

        return output

    def is_palindrome(self, s1: str) -> bool:
        i = 0
        j = len(s1) - 1

        while i < j:
            if s1[i] != s1[j]:
                return False
            i += 1
            j -= 1

        return True


def test() -> None:
    sol = Solution()
    print(sol.longestPalindrome(s="ababd"))
    sol = Solution()
    print(sol.longestPalindrome("abbc"))
    sol = Solution()
    print(sol.longestPalindrome("abc"))


if __name__ == "__main__":
    test()

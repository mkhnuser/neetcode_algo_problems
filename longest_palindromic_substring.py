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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        output_string = s[0]
        output_len = 1

        # NOTE: Odd length case.
        for i in range(len(s)):
            L = i - 1
            R = i + 1
            counter = 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                counter += 2
                L -= 1
                R += 1

            if counter > output_len:
                output_len = counter
                output_string = s[L + 1 : R]

        # NOTE: Even length case.
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                # NOTE: The initial two chars are not palindromes.
                continue

            L = i - 1
            R = i + 2
            counter = 2

            while L >= 0 and R < len(s) and s[L] == s[R]:
                counter += 2
                L -= 1
                R += 1

            if counter > output_len:
                output_len = counter

                if L == i and R == (i + 1):
                    # NOTE: The while loop has not executed even once, so just store two initial characters.
                    output_string = s[i : i + 2]
                else:
                    output_string = s[L + 1 : R]

        return output_string


def test() -> None:
    sol = Solution()
    print(sol.longestPalindrome("ababd"))
    sol = Solution()
    print(sol.longestPalindrome("abbc"))
    sol = Solution()
    print(sol.longestPalindrome("abc"))


if __name__ == "__main__":
    test()

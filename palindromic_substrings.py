class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if self.is_palindrome(substring):
                    output += 1
        return output

    def is_palindrome(self, string: str) -> bool:
        i = 0
        j = len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False

            i += 1
            j -= 1

        return True


class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            output += self.count_palindromes(s, i, i)
            output += self.count_palindromes(s, i, i + 1)

        return output

    def count_palindromes(self, s: str, L: int, R: int) -> int:
        res = 0
        while L >= 0 and R < len(s) and s[L] == s[R]:
            res += 1
            L -= 1
            R += 1
        return res


def test() -> None:
    sol = Solution()
    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))


if __name__ == "__main__":
    test()

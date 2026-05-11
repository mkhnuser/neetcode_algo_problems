import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.transform_string(s)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def transform_string(self, s):
        s = s.lower()
        res = []
        for char in s:
            if char not in string.punctuation and char != " ":
                res.append(char)
        return "".join(res)


def test():
    sol = Solution()
    s = "Was it a car or a cat I saw?"
    print(sol.isPalindrome(s))


if __name__ == "__main__":
    test()

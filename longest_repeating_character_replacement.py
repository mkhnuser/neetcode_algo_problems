class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0

        for i in range(len(s)):
            t = k
            L = i
            R = i

            # NOTE: Explore right.
            for j in range(i + 1, len(s)):
                if s[j] != s[i]:
                    if t <= 0:
                        break
                    t -= 1
                R += 1

            # NOTE: Explore left.
            for j in range(i - 1, -1, -1):
                if s[j] != s[i]:
                    if t <= 0:
                        break
                    t -= 1
                L -= 1

            output = max(output, R - L + 1)

        return output


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        output = 0
        counter = {}
        L = 0

        for R in range(len(s)):
            counter[s[R]] = counter.get(s[R], 0) + 1

            while (R - L + 1) - max(counter.values()) > k:
                counter[s[L]] -= 1
                L += 1

            output = max(output, R - L + 1)

        return output


def test() -> None:
    sol = Solution()
    s = "XYYX"
    k = 2
    print(sol.characterReplacement(s, k))

    s = "AAABABB"
    k = 1
    sol = Solution()
    print(sol.characterReplacement(s, k))


if __name__ == "__main__":
    test()

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        desired_mapping = {}

        for char in s1:
            if char not in desired_mapping:
                desired_mapping[char] = 0
            desired_mapping[char] += 1

        # NOTE: Create a sliding window which checks two strings for anagrams.
        s1_len = len(s1)
        window = {}
        L = 0

        for R in range(len(s2)):
            if (R - L + 1) > s1_len:
                if window[s2[L]] >= 2:
                    window[s2[L]] -= 1
                else:
                    del window[s2[L]]

                L += 1

            window[s2[R]] = window.get(s2[R], 0) + 1

            if window == desired_mapping:
                return True

        return False


def test() -> None:
    s1 = "abc"
    s2 = "lecaabee"
    sol = Solution()
    sol.checkInclusion(s1, s2)


if __name__ == "__main__":
    test()

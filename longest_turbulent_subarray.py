from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        R = 1
        output = 1
        prev_sign = ""

        while R < len(arr):
            prev_el = arr[R - 1]
            cur_el = arr[R]

            if cur_el > prev_el and prev_sign != "<":
                output = max(output, R - L + 1)
                R += 1
                prev_sign = "<"
            elif cur_el < prev_el and prev_sign != ">":
                output = max(output, R - L + 1)
                R += 1
                prev_sign = ">"
            else:
                R = R + 1 if prev_el == cur_el else R
                L = R - 1
                prev_sign = ""

        return output


def test() -> None:
    sol = Solution()
    sol.maxTurbulenceSize([2, 4, 3, 2, 2, 5, 1, 4])
    #                      2<4>3>2=2<5>1<4.


if __name__ == "__main__":
    test()

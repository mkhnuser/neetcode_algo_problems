class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x

        while L <= R:
            candidate = (L + R) // 2
            squared_candidate = candidate**2

            if squared_candidate == x:
                return candidate
            elif squared_candidate > x:
                R = candidate - 1
            else:
                L = candidate + 1

        return R

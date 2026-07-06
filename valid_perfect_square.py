class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 0
        R = num

        while L <= R:
            m = (L + R) // 2
            sq = m**2
            if sq == num:
                return True
            if sq > num:
                R = m - 1
            else:
                L = m + 1

        return False

class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x

        while L <= R:
            candidate = (L + R) // 2
            squared = candidate**2

            if squared == x:
                return candidate
            elif squared < x:
                L = candidate + 1
            else:
                R = candidate - 1

        return R


# NOTE: input = 4.
# [0, 4].
# candidate = 2 -> we are done.
#
#
#
# NOTE: input = 5.
# [0, 5].
# candidate = 2 -> 2 ** 2 == 4 < 5, so go to the right.
# [3, 5].
# candidate = 4 -> 4 ** 2 == 16 > 5, so go to the left.
# [3, 3].
# candidate = 3 -> 3 ** 2 == 9 > 5, so go to the left.
# [3, 2].
# Terminate and return R.

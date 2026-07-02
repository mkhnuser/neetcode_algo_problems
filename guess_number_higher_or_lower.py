# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n

        while L <= R:
            middle = (L + R) // 2
            response = guess(middle)
            if response == 0:
                return middle
            if response == -1:
                R = middle - 1
            if response == 1:
                L = middle + 1

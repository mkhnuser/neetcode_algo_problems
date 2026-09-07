class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        output = left

        for num in range(left + 1, right + 1):
            output &= num

            if output == 0:
                return 0

        return output


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right

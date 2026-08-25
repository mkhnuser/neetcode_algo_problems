from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            current_num = digits[i]

            if carry:
                current_num += carry

            if current_num >= 10:
                carry, new_digit = divmod(current_num, 10)
                digits[i] = new_digit
            else:
                digits[i] = current_num
                return digits

        if carry:
            digits.insert(0, carry)

        return digits


def test() -> None:
    sol = Solution()
    print(sol.plusOne([1, 2, 3, 4]))

    sol = Solution()
    print(sol.plusOne([9, 9, 9]))


if __name__ == "__main__":
    test()

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        a_pointer, b_pointer = len(a) - 1, len(b) - 1

        while a_pointer >= 0 or b_pointer >= 0 or carry > 0:
            a_digit = int(a[a_pointer]) if a_pointer >= 0 else 0
            b_digit = int(b[b_pointer]) if b_pointer >= 0 else 0

            total = a_digit + b_digit + carry
            res.append(total % 2)
            carry = total // 2

            a_pointer -= 1
            b_pointer -= 1

        res.reverse()
        return "".join(map(str, res))

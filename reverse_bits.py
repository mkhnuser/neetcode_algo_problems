class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        bits = []

        # NOTE: Let's collect the last bits of a number.
        while n > 0:
            bits.append(n & 1)
            n >>= 1

        # NOTE: Let's represent the binary representation of a number as a true int32.
        bits.reverse()
        prefix = [0] * (32 - len(bits))
        bits = prefix + bits

        # NOTE: Now let's perform the task of reversal.
        bits.reverse()
        output = 0
        i = 0

        while bits:
            last_bit = bits.pop()
            output += last_bit * (2**i)
            i += 1

        return output

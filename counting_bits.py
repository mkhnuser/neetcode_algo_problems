from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for number in range(0, n + 1):
            counter = 0

            while number > 0:
                counter += number & 1
                number >>= 1

            output.append(counter)

        return output

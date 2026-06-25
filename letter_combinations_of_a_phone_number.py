from typing import List


digit_to_letters_mapping = {
    0: [],
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d_array = [int(d) for d in digits]
        # output = []
        # index = 0
        # current_comb = ""
        #
        # self.recurse(d_array, output, current_comb, index)
        # return output
        return self.iterate(d_array)

    def recurse(
        self,
        d_array: List[int],
        output: List[str],
        current_comb: str,
        index: int,
    ) -> None:
        if index >= len(d_array):
            output.append(current_comb)
            return

        for letter in digit_to_letters_mapping[d_array[index]]:
            current_comb += letter
            self.recurse(d_array, output, current_comb, index + 1)
            current_comb = current_comb[:-1]

    def iterate(self, d_array: List[int]) -> List[str]:
        output = [""]
        for d in d_array:
            t = []
            for o in output:
                for letter in digit_to_letters_mapping[d]:
                    t.append(o + letter)
            output = t

        return output

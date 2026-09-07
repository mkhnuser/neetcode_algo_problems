from typing import List


digit_to_letters_mapping = {
    "0": "",
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "qprs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        return self.iterate(digits)

    def recurse(self, digits: str, p: int, s: str, output: list[str]) -> None:
        if p >= len(digits):
            output.append(s)
            return None

        current_digit = digits[p]
        letters = digit_to_letters_mapping[current_digit]
        for letter in letters:
            self.recurse(digits, p + 1, s + letter, output)

    def iterate(self, digits: str) -> list[str]:
        output = [""]

        for digit in digits:
            stage = []

            for string in output:
                for letter in digit_to_letters_mapping[digit]:
                    stage.append(string + letter)

            output = stage

        return output

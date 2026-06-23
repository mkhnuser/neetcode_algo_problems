from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_index = {char: i for i, char in enumerate(order)}
        char_indexes = [[char_to_index[char] for char in word] for word in words]

        for i in range(len(char_indexes) - 1):
            if not char_indexes[i] < char_indexes[i + 1]:
                return False

        return True

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # NOTE: mapping = {[char freq: sorted pairs]: [str1, str2, str3, ..., strn]}.
        # But how do you hash char freq? Represent it as a sorted tuple of tuples char:freq.

        mapping = {}

        for str_ in strs:
            key = self.compute_key_sorting(str_)
            if key not in mapping:
                mapping[key] = []
            mapping[key].append(str_)

        return [value for value in mapping.values()]

    def compute_key_hash_map(self, str_) -> tuple:
        freq_map = {}

        for char in str_:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1

        return tuple(sorted(freq_map.items()))

    def compute_key_ord(self, str_) -> tuple:
        counter = [0] * 26
        shift = ord("a")

        for char in str_:
            ordinal_number = ord(char)
            counter_index = ordinal_number - shift
            counter[counter_index] += 1

        return tuple(counter)

    def compute_key_sorting(self, str_) -> str:
        return "".join(sorted(str_))


def test():
    sol = Solution()
    print(sol.groupAnagrams(["cat", "tac", ""]))


if __name__ == "__main__":
    test()

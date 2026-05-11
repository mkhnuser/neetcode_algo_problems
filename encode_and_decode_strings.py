from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = []
        for str_ in strs:
            sizes.append(str(len(str_)))

        content_array = []
        for str_ in strs:
            content_array.append(str_)

        return ",".join(sizes) + "," + "#" + "".join(content_array)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes = []
        i = 0
        while s[i] != "#":
            size = ""
            while s[i] != ",":
                size += s[i]
                i += 1
            sizes.append(int(size))
            i += 1

        # NOTE: At this point, s[i] == "#".

        i += 1
        # NOTE: The first content character has been reached.
        output = []
        for size in sizes:
            output.append(s[i : i + size])
            i += size

        return output


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


def test():
    sol = Solution()
    some_input = ["Hello", "World"]
    encoded = sol.encode(some_input)
    print(encoded)
    print(sol.decode(encoded))


if __name__ == "__main__":
    test()

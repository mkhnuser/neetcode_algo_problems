import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 1 -> A.
        # 2 -> B.
        # ...
        # 26 -> Z.
        decimal_to_char = {
            i: char for i, char in enumerate(string.ascii_uppercase, start=1)
        }
        string_list = []

        while columnNumber > 0:
            # Given: 26.
            # divmod(26, 26) == (1, 0).
            # So:
            # We do: divmod(25, 26) == (0, 25).
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            string_list.append(decimal_to_char[remainder + 1])

        string_list.reverse()
        return "".join(string_list)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 1 -> A.
        # 2 -> B.
        # ...
        # 26 -> Z.
        string_list = []

        while columnNumber > 0:
            # Given: 26.
            # divmod(26, 26) == (1, 0).
            # So:
            # We do: divmod(25, 26) == (0, 25).
            columnNumber -= 1
            columnNumber, remainder = divmod(columnNumber, 26)
            string_list.append(chr(ord("A") + remainder))

        string_list.reverse()
        return "".join(string_list)

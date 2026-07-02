import string


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digits = []

        for char in s:
            if char in string.digits:
                digits.append(char)
            elif char == "[":
                if digits:
                    stack.append(int("".join(digits)))
                    digits.clear()

                stack.append(char)
            elif char == "]":
                # NOTE: pop off the stack until [ is encountered.
                char_list = []

                while stack and stack[-1] != "[":
                    popped = stack.pop()
                    char_list.append(popped)

                char_list.reverse()

                # NOTE: Clean up open bracket since it's no longer needed.
                stack.pop()

                multiplier = stack.pop()
                string_ = "".join(char_list)
                string_ = string_ * multiplier
                stack.append(string_)
            else:
                # NOTE: A plain char.
                stack.append(char)

        return "".join(stack)


def test() -> None:
    s = "2[a3[b]]c"
    sol = Solution()
    print(sol.decodeString(s))
    s = "axb3[z]4[c]"
    sol = Solution()
    print(sol.decodeString(s))
    s = "ab2[c]3[d]1[x]"
    sol = Solution()
    print(sol.decodeString(s))
    s = "10[a]"
    sol = Solution()
    print(sol.decodeString(s))


if __name__ == "__main__":
    test()

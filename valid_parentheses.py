class Solution:
    def isValid(self, s: str) -> bool:
        opening = set(["(", "[", "{"])
        closing = set([")", "]", "}"])
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False

                prev = stack.pop()
                if char == ")" and prev != "(":
                    return False
                if char == "]" and prev != "[":
                    return False
                if char == "}" and prev != "{":
                    return False

        return not stack

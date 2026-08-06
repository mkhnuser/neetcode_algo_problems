class Solution:
    def checkValidString(self, s: str) -> bool:
        open_parens = []
        stars = []

        for i, char in enumerate(s):
            if char == "(":
                open_parens.append(i)
            elif char == "*":
                stars.append(i)
            else:
                # NOTE: char == ")".
                if not open_parens and not stars:
                    return False
                if open_parens:
                    open_parens.pop()
                else:
                    stars.pop()

        while open_parens and stars:
            if open_parens.pop() > stars.pop():
                return False

        return not open_parens

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []
        self.recurse(n, output, stack, 0, 0)
        return output

    def recurse(
        self,
        n: int,
        output: list[str],
        stack: list[str],
        open_count: int,
        close_count: int,
    ) -> None:
        if open_count == close_count == n:
            output.append("".join(stack))
            return

        if open_count < n:
            stack.append("(")
            self.recurse(n, output, stack, open_count + 1, close_count)
            stack.pop()

        if close_count < open_count:
            stack.append(")")
            self.recurse(n, output, stack, open_count, close_count + 1)
            stack.pop()


# Input: n = 1
# Output: ["()"]
#
# Input: n = 2
# Output: ["()()", "(())"]
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


def test() -> None:
    sol = Solution()
    print(sol.generateParenthesis(1))
    sol = Solution()
    print(sol.generateParenthesis(2))
    sol = Solution()
    print(sol.generateParenthesis(3))


if __name__ == "__main__":
    test()

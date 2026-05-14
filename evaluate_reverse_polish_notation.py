from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        operands = []

        for token in tokens:
            if token in operators:
                second = operands.pop()
                first = operands.pop()

                if token == "+":
                    operands.append(first + second)
                elif token == "-":
                    operands.append(first - second)
                elif token == "*":
                    operands.append(first * second)
                elif token == "/":
                    operands.append(int(first / second))
            else:
                operands.append(int(token))

        return operands[-1]

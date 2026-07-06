from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        output = []

        for c in range(m):
            to_be_appended = []
            for r in range(n):
                to_be_appended.append(matrix[r][c])
            output.append(to_be_appended)

        return output


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        output: List[List[int | None]] = [[None for _ in range(n)] for __ in range(m)]

        for r in range(n):
            for c in range(m):
                output[c][r] = matrix[r][c]

        return output

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # NOTE: Indecies are 0-based.
        # NOTE:
        # row = 1, 2, 0, 1, 5.
        # square_row = 2, 0, 1.
        # sum(square_row) = sum(row) - 1 - 5.
        row_sums = [sum(row) for row in self.matrix]
        summation = 0
        for row_index in range(row1, row2 + 1):
            current_row = self.matrix[row_index]
            current_col_indecies = set(range(col1, col2 + 1))
            acc = sum(
                item
                for i, item in enumerate(current_row)
                if i not in current_col_indecies
            )
            summation += row_sums[row_index] - acc
        return summation

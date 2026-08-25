from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        rows_mapping = {r: False for r in range(n)}
        cols_mapping = {c: False for c in range(m)}

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows_mapping[i] = True
                    cols_mapping[j] = True

        for i in range(n):
            if rows_mapping[i]:
                matrix[i] = [0] * m

        for j in range(m):
            if cols_mapping[j]:
                for i in range(n):
                    row = matrix[i]
                    row[j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        extra_cell = False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # NOTE: Set a row for nullification.
                    if i == 0:
                        extra_cell = True
                    else:
                        matrix[i][0] = 0

                    # NOTE: Set a column for nullification.
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(n):
                matrix[i][0] = 0

        if extra_cell:
            for j in range(m):
                matrix[0][j] = 0


def test() -> None:
    sol = Solution()
    print(
        sol.setZeroes(
            matrix=[
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5],
            ]
        )
    )


if __name__ == "__main__":
    test()

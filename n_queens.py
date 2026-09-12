from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # NOTE: Create n by n matrix.
        matrix = [["." for _ in range(n)] for __ in range(n)]
        row_index = 0
        self.recurse(n, matrix, row_index, res)
        return res

    def recurse(
        self,
        n: int,
        matrix: List[List[str]],
        row_index: int,
        res: List[List[str]],
    ) -> None:
        # NOTE:
        # . . . .
        # . . . .
        # . . . .
        # . . . .

        if row_index >= n:
            res.append(["".join(row) for row in matrix])
            return None

        row = matrix[row_index]

        for pos, char in enumerate(row):
            if self.is_safe(row_index, pos, n, matrix):
                matrix[row_index][pos] = "Q"
                self.recurse(n, matrix, row_index + 1, res)
                matrix[row_index][pos] = "."

    def is_safe(self, i: int, j: int, n: int, matrix: List[List[str]]) -> bool:
        """Given coordinates (i, j), answers the question:

        If a queen is placed at (i, j), is it safe from all other queens?
        """
        # NOTE: Horizontal check.
        row = matrix[i]
        for char in row:
            if char == "Q":
                return False

        # NOTE: Vertical check.
        for row in matrix:
            for x, char in enumerate(row):
                if x == j and char == "Q":
                    return False

        # NOTE:
        # . . .
        # . . .
        # . . .

        # NOTE: Diagonal check: to the upper-left corner.
        a = i
        b = j
        while 0 <= a < n and 0 <= b < n:
            if matrix[a][b] == "Q":
                return False
            a -= 1
            b -= 1

        # NOTE: Diagonal check: to the upper-right corner.
        a = i
        b = j
        while 0 <= a < n and 0 <= b < n:
            if matrix[a][b] == "Q":
                return False
            a -= 1
            b += 1

        # NOTE: Diagonal check: to the lower-right corner.
        a = i
        b = j
        while 0 <= a < n and 0 <= b < n:
            if matrix[a][b] == "Q":
                return False
            a += 1
            b += 1

        # NOTE: Diagonal check: to the lower-left corner.
        a = i
        b = j
        while 0 <= a < n and 0 <= b < n:
            if matrix[a][b] == "Q":
                return False
            a += 1
            b -= 1

        return True


def test() -> None:
    sol = Solution()
    print(sol.solveNQueens(4))
    sol = Solution()
    print(sol.solveNQueens(1))
    sol = Solution()
    print(sol.solveNQueens(8))


if __name__ == "__main__":
    test()

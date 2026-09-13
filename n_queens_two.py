from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        # NOTE: Create n by n matrix.
        matrix = [["." for _ in range(n)] for __ in range(n)]
        row_index = 0
        return self.recurse(n, matrix, row_index)

    def recurse(
        self,
        n: int,
        matrix: List[List[str]],
        row_index: int,
    ) -> int:
        """Return True if a path is valid, return False otherwise."""
        # NOTE:
        # . . . .
        # . . . .
        # . . . .
        # . . . .

        if row_index >= n:
            return 1

        row = matrix[row_index]

        counter = 0
        for pos, char in enumerate(row):
            if self.is_safe(row_index, pos, n, matrix):
                matrix[row_index][pos] = "Q"
                counter += self.recurse(n, matrix, row_index + 1)
                matrix[row_index][pos] = "."

        return counter

    def is_safe(self, i: int, j: int, n: int, matrix: List[List[str]]) -> bool:
        """Given coordinates (i, j), answers the question:

        If a queen is placed at (i, j), is it safe from all other queens?
        """
        # NOTE: Horizontal check is unnecessary since you are placing only one queen on each row.
        # NOTE: Vertical check can be optimized to check only the top of the board.
        for x in range(i):
            if matrix[x][j] == "Q":
                return False

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

        # NOTE: No need to check a lower-right corner a lower-left corner since the board is populated top-to-bottom.

        return True


def test() -> None:
    sol = Solution()
    print(sol.totalNQueens(4))
    sol = Solution()
    print(sol.totalNQueens(1))
    sol = Solution()
    print(sol.totalNQueens(8))


if __name__ == "__main__":
    test()

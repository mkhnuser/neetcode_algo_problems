from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            # NOTE: An empty matrix has been given: [].
            return True

        n = len(board)
        m = len(board[0])

        # NOTE: Validate rows.
        for i in range(n):
            seen = set()
            for j in range(m):
                char = board[i][j]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # NOTE: Validate columns.
        for j in range(m):
            seen = set()
            for i in range(n):
                char = board[i][j]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # NOTE: Validate quadrants.
        row_boundaries = list(range(0, n + 1, 3))  # NOTE: 0, _, _, 3, _, _, 6, _, _, 9.
        column_boundaries = list(
            range(0, m + 1, 3)
        )  # NOTE: 0, _, _, 3, _, _, 6, _, _, 9.

        for i in range(1, len(row_boundaries)):
            row_start = row_boundaries[i - 1]
            row_end = row_boundaries[i]
            # NOTE:
            # 0 3
            # 3 6
            # 6 9

            for j in range(1, len(column_boundaries)):
                column_start = column_boundaries[j - 1]
                column_end = column_boundaries[j]
                # NOTE:
                # 0 3
                # 3 6
                # 6 9
                quadrant_rows = board[row_start:row_end]
                seen = set()
                for row in quadrant_rows:
                    for value in row[column_start:column_end]:
                        if value == ".":
                            continue
                        if value in seen:
                            return False
                        seen.add(value)

        return True


def test():
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol = Solution()
    print(sol.isValidSudoku(board))

    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol = Solution()
    print(sol.isValidSudoku(board))


if __name__ == "__main__":
    test()

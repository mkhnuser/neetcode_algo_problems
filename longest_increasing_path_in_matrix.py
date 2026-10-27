from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # NOTE: (r, c) -> Longest Increasing Path.

        for r in range(ROWS):
            for c in range(COLS):
                self.recurse(ROWS, COLS, matrix, dp, r, c, -1)

        return max(dp.values())

    def recurse(
        self,
        ROWS: int,
        COLS: int,
        matrix: list[list[int]],
        dp: dict,
        r: int,
        c: int,
        prev_val: int,
    ) -> int:
        if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev_val:
            return 0

        if (r, c) in dp:
            return dp[(r, c)]

        res = 1
        res = max(res, 1 + self.recurse(ROWS, COLS, matrix, dp, r + 1, c, matrix[r][c]))
        res = max(res, 1 + self.recurse(ROWS, COLS, matrix, dp, r - 1, c, matrix[r][c]))
        res = max(res, 1 + self.recurse(ROWS, COLS, matrix, dp, r, c + 1, matrix[r][c]))
        res = max(res, 1 + self.recurse(ROWS, COLS, matrix, dp, r, c - 1, matrix[r][c]))
        dp[(r, c)] = res
        return res

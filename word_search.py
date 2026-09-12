from typing import List


DIRECTIONS = (
    (+1, 0),
    (0, +1),
    (-1, 0),
    (0, -1),
)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = word.lower()
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                board[i][j] = board[i][j].lower()

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and self.recurse(
                    board, n, m, word, i, j, 0, set()
                ):
                    return True

        return False

    def recurse(
        self,
        board: List[List[str]],
        n: int,
        m: int,
        word: str,
        i: int,
        j: int,
        depth: int,
        visited: set,
    ) -> bool:
        if depth == len(word):
            return True

        if (
            i < 0
            or i >= n
            or j >= m
            or j < 0
            or word[depth] != board[i][j]
            or (i, j) in visited
        ):
            return False

        visited.add((i, j))

        res = False

        for dir in DIRECTIONS:
            i_incr, j_incr = dir
            res = res or self.recurse(
                board,
                n,
                m,
                word,
                i + i_incr,
                j + j_incr,
                depth + 1,
                visited,
            )

        visited.remove((i, j))

        return res

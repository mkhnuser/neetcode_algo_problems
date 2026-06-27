from typing import List
from queue import Queue


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


X = "X"
O = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # NOTE:
        # Go over borders.
        # Explore islands and mark them as safe.
        # Delete all unsafe islands.

        if not board:
            return

        n = len(board)
        m = len(board[0])
        safety_net = set()

        # NOTE: Top border.
        for c in range(m):
            if board[0][c] == O:
                safety_net.update(self.bfs(0, c, board, n, m))

        # NOTE: Right border.
        for r in range(n):
            if board[r][m - 1] == O:
                safety_net.update(self.bfs(r, m - 1, board, n, m))

        # NOTE: Bottom border.
        for c in range(m):
            if board[n - 1][c] == O:
                safety_net.update(self.bfs(n - 1, c, board, n, m))

        # NOTE: Left border.
        for r in range(n):
            if board[r][0] == O:
                safety_net.update(self.bfs(r, 0, board, n, m))

        for i in range(n):
            for j in range(m):
                if board[i][j] == O and (i, j) not in safety_net:
                    board[i][j] = X

    def bfs(
        self,
        i: int,
        j: int,
        board: List[List[str]],
        n: int,
        m: int,
    ) -> set[tuple[int, int]]:
        q = Queue()
        q.put((i, j))
        visited = set()
        visited.add((i, j))

        while q.qsize() > 0:
            i, j = q.get()

            for dir in DIRECTIONS:
                i_incr, j_incr = dir
                next_i = i + i_incr
                next_j = j + j_incr

                if (
                    next_i < 0
                    or next_i >= n
                    or next_j < 0
                    or next_j >= m
                    or board[next_i][next_j] == X
                    or (next_i, next_j) in visited
                ):
                    continue

                q.put((next_i, next_j))
                visited.add((next_i, next_j))

        return visited


def test():
    sol = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print(sol.solve(board))


if __name__ == "__main__":
    test()

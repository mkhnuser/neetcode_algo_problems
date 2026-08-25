from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L, R = 0, len(matrix) - 1

        while L < R:
            for i in range(R - L):
                T, B = L, R

                # save the topleft
                top_left = matrix[T][L + i]

                # move bottom left into top left
                matrix[T][L + i] = matrix[B - i][L]

                # move bottom right into bottom left
                matrix[B - i][L] = matrix[B][R - i]

                # move top right into bottom right
                matrix[B][R - i] = matrix[T + i][R]

                # move top left into top right
                matrix[T + i][R] = top_left

            R -= 1
            L += 1

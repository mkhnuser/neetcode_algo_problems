from typing import List
from collections import defaultdict


class CountSquares:
    def __init__(self):
        self.points_counter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points_counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        output = 0
        px, py = point

        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue

            # NOTE: A diagonal point has been found.
            output += self.points_counter[(x, py)] * self.points_counter[(px, y)]

        return output

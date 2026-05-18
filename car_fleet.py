from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # NOTE: target = miles.
        # position: list[int] = position in miles.
        # speed: list[int] = miles per hour speed.

        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            hours_to_destination = (target - p) / s
            stack.append(hours_to_destination)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                # NOTE: "Concatenate" two cars.

        return len(stack)

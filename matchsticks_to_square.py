from typing import List


UP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)

        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        current_position = [0, 0, 0, 0]  # NOTE: Represents (up, right, bottom, left).
        matchsticks.sort(reverse=True)

        return self.recurse(
            matchsticks,
            0,
            current_position,
            side_length,
        )

    def recurse(
        self,
        matchsticks: List[int],
        i: int,
        current_position: list[int],
        side_length: int,
    ) -> bool:
        if i >= len(matchsticks):
            first_coord = current_position[0]
            for pos in current_position:
                if pos != first_coord:
                    return False
            return True

        current_matchstick = matchsticks[i]

        for direction in (UP, RIGHT, BOTTOM, LEFT):
            if current_position[direction] + current_matchstick <= side_length:
                current_position[direction] += current_matchstick
                if self.recurse(matchsticks, i + 1, current_position, side_length):
                    return True
                current_position[direction] -= current_matchstick

        return False


def test() -> None:
    sol = Solution()
    matchsticks = [1, 3, 4, 2, 2, 4]
    print(sol.makesquare(matchsticks))
    # NOTE: The solution: 1 up, 3 up, 4 to the right, 2 down, 2 down, 4 to the left.

    sol = Solution()
    matchsticks = [1, 5, 6, 3]
    print(sol.makesquare(matchsticks))


if __name__ == "__main__":
    test()

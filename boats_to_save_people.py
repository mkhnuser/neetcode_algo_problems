from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        pairs = 0
        people.sort()

        lp = 0
        rp = len(people) - 1

        while lp < rp:
            lw = people[lp]
            rw = people[rp]

            if lw + rw <= limit:
                pairs += 1
                lp += 1
                rp -= 1
            else:
                rp -= 1

        taken = pairs * 2
        boats = pairs + (len(people) - taken)
        return boats


def test() -> None:
    sol = Solution()
    people = [5, 1, 4, 2]
    limit = 6
    print(sol.numRescueBoats(people, limit))

    people = [1, 3, 2, 3, 2]
    limit = 3
    print(sol.numRescueBoats(people, limit))


if __name__ == "__main__":
    test()

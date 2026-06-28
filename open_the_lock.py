from queue import Queue
from typing import List


DIRECTIONS = (+1, -1)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        q = Queue()
        q.put(("0000", 0))
        visited = set()

        while q.qsize() > 0:
            c, dist = q.get()

            if c == target:
                return dist

            c = list(c)

            for i in range(len(c)):
                d = int(c[i])

                for dir in DIRECTIONS:
                    candidate = (d + dir) % 10
                    c_copy = c.copy()
                    c_copy[i] = str(candidate)
                    c_copy = "".join(c_copy)
                    if c_copy not in visited and c_copy not in deadends:
                        q.put((c_copy, dist + 1))
                        visited.add(c_copy)

        return -1


def test():
    deadends = ["1111", "0120", "2020", "3333"]
    target = "5555"
    sol = Solution()
    print(sol.openLock(deadends, target))


if __name__ == "__main__":
    test()

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            while s and a < 0 and s[-1] > 0:
                diff = a + s[-1]

                if diff < 0:
                    s.pop()
                elif diff == 0:
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(a)

        return s

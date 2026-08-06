from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            if self.can_form_a_cycle(i, gas, cost, n):
                return i

        return -1

    def can_form_a_cycle(self, i: int, gas: List[int], cost: List[int], n: int) -> bool:
        tank = 0

        for _ in range(n):
            tank += gas[i]
            tank -= cost[i]

            if tank < 0:
                return False

            i = (i + 1) % n

        return True


def test() -> None:
    gas = [1, 2, 3, 4]
    cost = [2, 2, 4, 1]
    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))

    gas = [1, 2, 3]
    cost = [2, 3, 2]
    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))


if __name__ == "__main__":
    test()

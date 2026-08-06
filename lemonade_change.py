from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collected_fives = []
        collected_tens = []
        collected_twenties = []

        for bill in bills:
            if bill == 5:
                collected_fives.append(5)
                continue

            if bill == 10:
                if not collected_fives:
                    return False

                collected_fives.pop()
                collected_tens.append(10)
                continue

            if bill == 20:
                acc = 0

                if collected_tens:
                    # NOTE: There might not be none tens.
                    # In this case, fall back to giving fives only.
                    acc += collected_tens.pop()

                while collected_fives and acc < 15:
                    acc += collected_fives.pop()

                if acc != 15:
                    return False

                collected_twenties.append(20)
                continue

            raise RuntimeError("Error bill has been received!")

        return True


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0

        for b in bills:
            if b == 5:
                fives += 1
                continue
            elif b == 10:
                if not fives:
                    return False
                fives -= 1
                tens += 1
                continue
            if tens:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
            if fives < 0:
                return False

        return True


def test() -> None:
    sol = Solution()
    print(sol.lemonadeChange([5, 10, 5, 5, 20]))
    print(sol.lemonadeChange([5, 20, 10, 5]))
    print(sol.lemonadeChange([5, 10, 5, 20, 5, 5, 5, 20, 5, 5]))


if __name__ == "__main__":
    test()

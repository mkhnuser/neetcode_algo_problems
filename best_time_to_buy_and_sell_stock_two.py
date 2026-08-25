from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        diff = 0

        for i in range(1, len(prices)):
            prev_price = prices[i - 1]
            current_price = prices[i]

            if prev_price < current_price:
                # NOTE: Start your trading journey.
                diff += current_price - prev_price
            else:
                profit += diff
                diff = 0

        return profit if profit >= (profit + diff) else (profit + diff)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0

        for i in range(1, len(prices)):
            prev_price = prices[i - 1]
            current_price = prices[i]

            if prev_price < current_price:
                diff += current_price - prev_price

        return diff


def test() -> None:
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))

    sol = Solution()
    print(sol.maxProfit(prices=[1, 2, 3, 4, 5]))

    sol = Solution()
    print(sol.maxProfit(prices=[2, 1, 2, 0, 1]))


if __name__ == "__main__":
    test()

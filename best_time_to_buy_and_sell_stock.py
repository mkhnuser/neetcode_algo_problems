from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # NOTE: A single day to buy, a single day in the future to sell.
        max_profit = float("-inf")

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                buy_price = prices[i]
                sell_price = prices[j]
                profit = sell_price - buy_price

                if profit > max_profit:
                    max_profit = profit

        return max(max_profit, 0)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # NOTE: A single day to buy, a single day in the future to sell.
        L = 0
        R = 1
        max_profit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                if profit > max_profit:
                    max_profit = profit
            else:
                # NOTE: No point to buy high and sell low.
                L = R

            R += 1

        return max_profit


def test():
    prices = [10, 1, 5, 6, 7, 1]
    sol = Solution()
    print(sol.maxProfit(prices))
    prices = [10, 8, 7, 5, 2]
    sol = Solution()
    print(sol.maxProfit(prices))


if __name__ == "__main__":
    test()

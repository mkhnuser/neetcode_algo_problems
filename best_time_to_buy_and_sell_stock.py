from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                current_profit = prices[j] - prices[i]
                if current_profit > p:
                    p = current_profit

        return p


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                c = prices[r] - prices[l]
                p = max(p, c)
            else:
                l = r
            r += 1

        return p


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        buy_price = prices[0]

        for sell_price in prices:
            p = max(p, sell_price - buy_price)
            buy_price = min(buy_price, sell_price)

        return p

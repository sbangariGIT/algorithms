class Solution:
    def maxProfit(self, prices: int) -> int:
        max_profit = 0
        least_price = float('inf')
        for price in prices:
            least_price = min(price, least_price)
            max_profit = max(max_profit, price - least_price)
        return max_profit
        
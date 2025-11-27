class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            bought = prices[buy]
            sold = prices[sell]

            if bought < sold:
                max_profit = max(max_profit, sold - bought)
                sell += 1
            else:
                buy = sell
                sell += 1
        
        return max_profit
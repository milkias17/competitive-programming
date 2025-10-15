class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        min_bought = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cur_sold = prices[i]
            if cur_sold <= min_bought:
                min_bought = cur_sold
                continue
            
            max_profit = max(max_profit, cur_sold - min_bought)
        
        return max_profit
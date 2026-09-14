class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices.copy()

        for i, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                ans[stack.pop()] -= price
            
            stack.append(i)
        
        return ans

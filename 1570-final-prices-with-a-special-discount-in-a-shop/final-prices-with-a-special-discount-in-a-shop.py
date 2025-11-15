class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()
        stack = []
        for i in range(len(answer) - 1, -1, -1):
            while len(stack) > 0 and stack[-1] > prices[i]:
                stack.pop()
            
            if len(stack) == 0:
                stack.append(prices[i])
                continue
            
            answer[i] -= stack[-1]
            stack.append(prices[i])
        
        return answer
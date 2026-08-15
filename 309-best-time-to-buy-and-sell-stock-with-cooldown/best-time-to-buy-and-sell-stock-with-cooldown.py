class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = {"cooldown": 0, "sell": 0, "buy": 0}
        nxt = tmp.copy()
        for i in range(len(prices) - 1, -1, -1):
            cur = tmp.copy()
            for state in cur:
                if state == "cooldown":
                    cur[state] = nxt["buy"]
                elif state == "buy":
                    cur[state] = max(-prices[i] + nxt["sell"],  nxt["buy"])
                else:
                    cur[state] = max(prices[i] + nxt["cooldown"],  nxt["sell"])
            
            nxt = cur
        
        return nxt["buy"]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for a in range(amount + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 0
        
        for a in range(1, amount + 1):
            dp[-1][a] = -1
        
        current = [-1 for _ in range(amount + 1)]
        nxt = [-1 for _ in range(amount + 1)]
        current[0] = 0
        nxt[0] = 0

        
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                opt1 = -1
                if a - coins[i] >= 0:
                    opt1 = current[a - coins[i]]
                opt2 = nxt[a]

                res = None
                if opt1 == -1:
                    res = opt2
                elif opt2 == -1:
                    res = 1 + opt1
                else:
                    res = min(1 + opt1, opt2)
                
                current[a] = res
            
            nxt = current
            current = [-1 for _ in range(amount + 1)]
            current[0] = 0
        
        return nxt[amount]


            
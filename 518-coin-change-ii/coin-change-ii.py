class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        current = [0] * (amount + 1)
        nxt = [0] * (amount + 1)
        current[0] = 1
        nxt[0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                opt1 = current[a - coins[i]] if a - coins[i] >= 0 else 0
                opt2 = nxt[a]
                current[a] = opt1 + opt2
            
            nxt = current
            current = [0] * (amount + 1)
            current[0] = 1


        return nxt[amount]

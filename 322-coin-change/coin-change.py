class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def min_coins(target: int) -> int:
            if target < 0:
                return float("inf")
            
            if target == 0:
                return 0
            
            if target in memo:
                return memo[target]
            
            res = float("inf")
            for coin in coins:
                tmp = min_coins(target - coin)
                if tmp != float("inf"):
                    res = min(res, tmp + 1)
            
            memo[target] = res
            return memo[target]
        
        res = min_coins(amount)
        return res if res != float("inf") else -1
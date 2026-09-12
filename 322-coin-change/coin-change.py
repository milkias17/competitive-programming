class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        INF = float("inf")

        def dp(target):
            if target == 0:
                return 0
            
            if target < 0:
                return INF


            if target in memo:
                return memo[target]            
            
            res = INF
            for coin in coins:
                tmp = dp(target - coin)
                if tmp != INF:
                    res = min(res, 1 + tmp)

            memo[target] = res
            return res
        
        res = dp(amount)
        if res == INF:
            return -1

        return res

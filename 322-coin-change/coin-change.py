class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i, remaining):
            if remaining == 0:
                return 0

            if i >= len(coins) or remaining < 0:
                return float("inf")

            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            res =  min(
                1 + dp(i, remaining - coins[i]),
                1 + dp(i + 1, remaining - coins[i]),
                dp(i + 1, remaining)
            )
            memo[(i, remaining)] = res
            return res
        
        res = dp(0, amount)
        if res == float("inf"):
            return -1

        return res

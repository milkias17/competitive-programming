class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, target):
            if target < 0 or i >= len(coins):
                return 0
            
            if target == 0:
                return 1
            
            return dp(i, target - coins[i]) + dp(i + 1, target)
        
        return dp(0, amount)
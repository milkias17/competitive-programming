class Solution:
    def climbStairs(self, n: int) -> int:
        
        def backtrack(cur, memo={}):
            if cur > n:
                return 0
            if cur == n:
                return 1

            if cur not in memo:
                memo[cur] = backtrack(cur + 1) + backtrack(cur + 2)
            
            return memo[cur]
        
        count = backtrack(0)
        return count
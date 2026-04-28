class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [cost[-2], cost[-1]]
        i = len(cost) - 3

        while i >= 0:
            tmp = dp[0]
            dp[0] = cost[i] + min(dp)
            dp[1] = tmp
            i -= 1
        
        return min(dp)
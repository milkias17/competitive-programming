class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(i, memo={}):
            if i >= len(cost):
                return 0
                
            if i == len(cost) - 1:
                return cost[i]

            if i not in memo:
                memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]

        return min(dfs(0), dfs(1))
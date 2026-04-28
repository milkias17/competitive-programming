class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev1, prev2 = 0, 0

        for coins in cost:
            current = coins + min(prev1, prev2)

            prev1, prev2 = current, prev1
        
        return min(prev1, prev2)
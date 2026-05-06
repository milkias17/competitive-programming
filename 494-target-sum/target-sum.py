class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, remainder):
            if i == len(nums):
                return 1 if remainder == 0 else 0
            
            if (i, remainder) in memo:
                return memo[(i, remainder)]

            res = dfs(i + 1, remainder - nums[i]) + dfs(i + 1, remainder + nums[i])
            memo[(i, remainder)] = res
            return res
        
        return dfs(0, target)
            
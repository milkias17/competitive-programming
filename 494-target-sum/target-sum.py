class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        memo = [[-1 for _ in range((2 * (total + 1)) + 1)] for _ in range(len(nums) + 1)]

        def dfs(i, cur_sum):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            if memo[i][cur_sum + total] != -1:
                return memo[i][cur_sum + total]

            res = dfs(i + 1, cur_sum - nums[i]) + dfs(i + 1, cur_sum + nums[i])
            memo[i][cur_sum + total] = res
            return res
        
        return dfs(0, 0)
            
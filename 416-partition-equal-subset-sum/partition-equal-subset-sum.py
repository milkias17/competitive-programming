class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2

        memo = [[None for t in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            memo[i][0] = True
            
        for t in range(1, target + 1):
            memo[-1][t] = False
        
        for i in range(len(nums) - 1, -1, -1):
            cur = nums[i]
            for t in range(target + 1):
                res = memo[i + 1][t]
                if t - cur >= 0:
                    res = res or memo[i + 1][t - cur]
                
                memo[i][t] = res
        
        return memo[0][target]
                

        # def dfs(i, target):
        #     if target == 0:
        #         return True
        #     if target < 0:
        #         return False

        #     if i >= len(nums):
        #         return False
            
        #     if memo[i][target] is not None:
        #         return memo[i][target]
            
            
        #     res =  dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        #     memo[i][target] = res
        #     return res
        
        # return dfs(0, target)

        # [1, 5, 11, 5] -> True(11)
        # [1, 2, 3, 5] -> False
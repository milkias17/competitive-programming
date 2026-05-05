class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        memo = {}

        def dp(i, target):
            if target == 0:
                return True
            
            if target < 0 or i >= len(nums):
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]

            
            res = dp(i + 1, target - nums[i]) or dp(i + 1, target)
            memo[(i, target)] = res
            return res

        return dp(0, s // 2)
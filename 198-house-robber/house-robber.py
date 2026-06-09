class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0] # prev, prev prev
        for i in range(len(nums) - 1, -1, -1):
            opt1 = nums[i] + dp[1]
            opt2 =  dp[0]
            dp[1] = dp[0]
            dp[0] = max(opt1, opt2)
        
        return dp[0]
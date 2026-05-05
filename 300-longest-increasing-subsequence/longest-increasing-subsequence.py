class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        self.longest = float("-inf")

        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dp(j))
            
            memo[i] = res
            return res
        
        for i in range(len(nums)):
            self.longest = max(self.longest, dp(i))
        
        return self.longest
        
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        
        return prefix
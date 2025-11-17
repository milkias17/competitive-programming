class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        while len(nums) > 1:
            new_nums = []
            for i in range(0, len(nums) - 1):
                new_nums.append((nums[i] + nums[i+1]) % 10)
            nums = new_nums
        
        return nums[0]
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        hills = 0
        valleys = 0
        while i < len(nums):
            prev = i - 1
            while prev >= -1 and nums[prev] == nums[i]:
                prev -= 1
            
            if prev < 0:
                i += 1
                continue
            
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            
            if next_i >= len(nums):
                break
            
            if nums[prev] < nums[i] and nums[next_i] < nums[i]:
                hills += 1
            if nums[prev] > nums[i] and nums[next_i] > nums[i]:
                valleys += 1
            
            i = next_i
        
        return hills + valleys

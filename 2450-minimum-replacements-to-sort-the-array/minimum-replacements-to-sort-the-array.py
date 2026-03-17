import math

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        min_val = float("inf")

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min_val:
                min_val = min(min_val, nums[i])
                continue
            
            k = math.ceil(nums[i] / min_val)
            count += k - 1
            min_val = min(min_val, nums[i] // k)
        
        return count
            
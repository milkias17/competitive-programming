class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = 0
        ops = 0
        for right in range(len(nums)):
            if right - left + 1 < 3:
                continue
            
            if nums[left] == 0:
                ops += 1
                for i in range(left, right + 1):
                    nums[i] = 1 if nums[i] == 0 else 0
            
            left += 1
        
        if 0 not in nums:
            return ops
        else:
            return -1


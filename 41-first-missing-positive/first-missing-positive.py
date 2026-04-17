class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cur = 0
        while cur < len(nums):
            idx = nums[cur] - 1

            if nums[cur] <= 0 or idx >= len(nums) or idx == cur or nums[idx] == nums[cur]:
                cur += 1
                continue
            
            nums[idx], nums[cur] = nums[cur], nums[idx]
        
        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1
        
        return len(nums) + 1
            
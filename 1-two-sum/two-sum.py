class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = {}
        for i, num in enumerate(nums):
            if target - num in num_idx_map:
                return [num_idx_map[target - num], i]
            
            num_idx_map[num] = i
        
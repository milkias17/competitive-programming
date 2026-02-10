class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = {}
        for i, num in enumerate(nums):
            num_idx_map[num] = i
        
        for i, num in enumerate(nums):
            need = target - num
            if need in num_idx_map and num_idx_map[need] != i:
                return [i, num_idx_map[need]]
        
        return []
        
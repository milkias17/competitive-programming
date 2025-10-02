class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx_map = {}
        for i, num in enumerate(nums):
            if target - num in num_idx_map:
                return [i, num_idx_map[ target - num]]
            num_idx_map[num] = i
        

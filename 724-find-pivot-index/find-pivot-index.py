class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix = []
        for i, num in enumerate(nums):
            if i == 0:
                left_prefix.append(num)
            else:
                left_prefix.append(left_prefix[i - 1] + num)
        
        right_prefix = nums.copy()
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_prefix[i] = nums[i]
            else:
                right_prefix[i] = nums[i] + right_prefix[i + 1]
        
        for i in range(len(left_prefix)):
            if left_prefix[i] == right_prefix[i]:
                return i
        
        return -1

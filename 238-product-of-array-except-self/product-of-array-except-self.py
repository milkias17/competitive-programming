class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = []
        prefix_right = [None] * len(nums)

        cur = 1
        for i in range(len(nums)):
            prefix_left.append(cur)
            cur *= nums[i]
        
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_right[i] = cur
            cur *= nums[i]
        
        return [prefix_left[i] * prefix_right[i] for i in range(len(prefix_left))]

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_p = []
        right_p = [1] * len(nums)
        i = 0
        while i < len(nums):
            if len(left_p) == 0:
                left_p.append(nums[i])
            else:
                left_p.append(left_p[i - 1] * nums[i])
            
            right = len(nums) - 1 - i
            if i == 0:
                right_p[right] = nums[right]
            else:
                right_p[right] = right_p[right + 1] * nums[right]

            i += 1
        
        res = []
        for i in range(len(nums)):
            left_product = 1
            if i > 0:
                left_product = left_p[i - 1]

            right_product = 1
            if i < len(nums) - 1:
                right_product = right_p[i + 1]
            
            res.append(left_product * right_product)
        
        return res

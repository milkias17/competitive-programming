class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        cur = 1

        for right in range(len(nums)):
            cur *= nums[right]

            while left <= right and cur >= k:
                cur /= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
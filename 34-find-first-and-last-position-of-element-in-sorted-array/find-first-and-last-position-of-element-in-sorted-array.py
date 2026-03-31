class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = None
        end = None

        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (right + left) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        
        if left == -1 or nums[left] != target:
            return [-1, -1]
        
        end = left

        left = -1
        right = len(nums)        
        while left + 1 < right:
            mid = (right + left) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        start = right

        return [start, end]

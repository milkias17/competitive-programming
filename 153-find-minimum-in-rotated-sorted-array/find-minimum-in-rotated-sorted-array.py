class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = float("inf")

        while left <= right:
            mid = left + (right - left) // 2

            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                res = min(res, nums[left])
                left = mid + 1
            else:
                right = mid - 1
        
        return res
                
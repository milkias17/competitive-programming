class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left = 0
        for right in range(len(nums)):
            if right - left + 1 == 3:
                if nums[right] + nums[right - 1] > nums[left]:
                    return nums[left] + nums[left + 1] + nums[right]

                left += 1
        
        return 0
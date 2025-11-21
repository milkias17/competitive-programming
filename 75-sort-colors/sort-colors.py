class Solution:
    def quick_sort(self, nums: List[int], start, end):
        if start >= end:
            return

        pivot = end
        left = start
        for right in range(start, end):
            if nums[right] < nums[pivot]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        nums[left], nums[pivot] = nums[pivot], nums[left]
        pivot = left
        self.quick_sort(nums, start, pivot - 1)
        self.quick_sort(nums, pivot + 1, end)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)
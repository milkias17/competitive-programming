class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick_sort(start, end):
            if start >= end:
                return
                
            pivot = nums[end]
            left, cur = start, start
    
            while cur < end:
                if nums[cur] <= pivot:
                    nums[cur], nums[left] = nums[left], nums[cur]
                    left += 1
                
                cur += 1
            
            nums[left], nums[end] = nums[end], nums[left]
            quick_sort(start, left - 1)
            quick_sort(left + 1, end)
        
        quick_sort(0, len(nums) - 1)

        
        
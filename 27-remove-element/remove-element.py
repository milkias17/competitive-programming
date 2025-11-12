class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        i = 0
        end = len(nums) - 1
        while i <= end:
            if nums[i] == val:
                count -= 1
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1
        
        return count
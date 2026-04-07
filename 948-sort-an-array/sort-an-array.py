class Solution:
    def merge(self, left, right):
        new_arr = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                new_arr.append(left[i])
                i += 1
            else:
                new_arr.append(right[j])
                j += 1
        
        new_arr.extend(left[i:])
        new_arr.extend(right[j:])
        return new_arr

    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

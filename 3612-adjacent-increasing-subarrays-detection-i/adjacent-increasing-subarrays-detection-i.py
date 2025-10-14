class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        left = 0
        right = left + k
        while right < len(nums) - k + 1:
            cur = left
            left_increasing = True
            right_increasing = True
            while cur < right - 1:
                if nums[cur] >= nums[cur + 1]:
                    left_increasing = False
                    break
                cur += 1
            if not left_increasing:
                left += 1
                right += 1
                continue
            
            cur = right
            while cur < right + k - 1:
                if nums[cur] >= nums[cur + 1]:
                    right_increasing = False
                    break
                cur += 1
            
            if not right_increasing:
                left += 1
                right += 1
                continue
            
            return True
        
        return False
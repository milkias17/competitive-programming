class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        els = Counter()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                els[nums[left]] -= 1
                if els[nums[left]] <= 0:
                    del els[nums[left]]
                
                left += 1
            

            if nums[right] in els:
                return True

            els[nums[right]] += 1

        
        return False


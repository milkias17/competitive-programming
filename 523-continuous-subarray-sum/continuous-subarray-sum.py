class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefix = {0: -1}
        cur = 0

        for i, num in enumerate(nums):
            cur += num
            if (cur % k) in prefix and i - prefix[cur % k] >= 2:
                return True
            
            if cur % k not in prefix:
                prefix[cur % k] = i
        
        return False
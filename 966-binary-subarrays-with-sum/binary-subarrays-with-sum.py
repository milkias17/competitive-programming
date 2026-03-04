class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = Counter()
        counter[0] += 1
        count = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            
            if count - goal in counter:
                res += counter[count - goal]
                
            counter[count] += 1
        
        return res
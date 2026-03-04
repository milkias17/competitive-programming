class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = float("inf")
        cur = 0
        for num in nums:
            cur += num
            min_prefix = min(min_prefix, cur)
        
        if min_prefix <= 0:
            return 1 - min_prefix
        else:
            return 1
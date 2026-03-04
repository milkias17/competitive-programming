class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_idx = None
        res = None
        max_sum = float("-inf")
        prefix = []

        cur = 0
        for i, num in enumerate(nums):
            cur += num
            prefix.append(cur)
            
            cur_sum = cur
            if min_idx is not None:
                cur_sum -= prefix[min_idx]
            
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = (min_idx + 1 if min_idx is not None else 0, i)
            
            if cur < 0:
                if min_idx is None:
                    min_idx = i
                elif cur < prefix[min_idx]:
                    min_idx = i
        
        print(res)
        return max_sum
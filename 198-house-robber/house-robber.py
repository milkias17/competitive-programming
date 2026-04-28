class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev1, prev2 = max(nums[-2], nums[-1]), nums[-1]

        for i in range(len(nums) - 3, -1, -1):
            cur = max(nums[i] + prev2, prev1)

            prev1, prev2 = cur, prev1
        
        return max(prev1, prev2)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = None
        nums.sort()
        count = nums[-1]

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                dup = nums[i]
            count += nums[i]
        
        should = (len(nums) * (len(nums) + 1)) // 2
        return [dup, should - count + dup]

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left = 0
        right = left + 2
        cur = set()
        ops = 0

        while right < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1
            right = left + 2
            if right >= len(nums):
                return ops if 0 not in nums else -1
            
            tmp = left
            while tmp <= right:
                if nums[tmp] == 0:
                    nums[tmp] = 1
                else:
                    nums[tmp] = 0
                tmp += 1
            
            left += 1
            right = left + 2
            ops += 1
        
        return ops if 0 not in nums else -1

            


            

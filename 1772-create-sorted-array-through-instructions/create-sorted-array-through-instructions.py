class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        cost = 0
        mod = pow(10, 9) + 7

        for instruction in instructions:
            left = -1
            right = len(nums)

            while left + 1 < right:
                mid = left + (right - left) // 2

                if nums[mid] < instruction:
                    left = mid
                else:
                    right = mid
            
            less_than = left + 1
            left = -1
            right = len(nums)
            while left + 1 < right:
                mid = left + (right - left) // 2

                if nums[mid] > instruction:
                    right = mid
                else:
                    left = mid

            greater_than = len(nums) - right
            cost = (cost + min(greater_than, less_than)) % mod
            nums.insert(left + 1, instruction)
        
        return cost % mod
            
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        res = []
        for val, idx in queries:
            prev_even = nums[idx] % 2 == 0
            prev_val = nums[idx]
            nums[idx] += val

            if prev_even:
                even_sum -= prev_val
            
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            
            res.append(even_sum)
        
        return res


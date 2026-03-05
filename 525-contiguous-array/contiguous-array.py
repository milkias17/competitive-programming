class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {0: -1}
        num_zeroes = 0
        num_ones = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                num_zeroes += 1
            else:
                num_ones += 1
            
            if num_ones - num_zeroes in counter:
                max_len = max(max_len, i - (counter[num_ones - num_zeroes] + 1) + 1)
            else:
                counter[num_ones - num_zeroes] = i
        
        return max_len
            
            
            

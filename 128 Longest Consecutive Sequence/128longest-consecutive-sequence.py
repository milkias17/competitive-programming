class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u_nums = set(nums)
        longest = 0
        for num in u_nums:
            if num - 1 in u_nums:
                continue
            
            length = 1
            while num + length in u_nums:
                length += 1
            
            longest = max(longest, length)
        
        return longest
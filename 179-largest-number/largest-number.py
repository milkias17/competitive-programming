from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare_strings(s1, s2):
            s1 = str(s1)
            s2 = str(s2)
            if s2 + s1 < s1 + s2:
                return -1
            elif s2 + s1 > s1 + s2:
                return 1
            else:
                return 0
        
        nums.sort(key=cmp_to_key(compare_strings))
        if nums[0] == 0:
            return "0"
        return "".join(map(str, nums))
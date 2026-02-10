class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            sep_list = list(str(num))
            for sep in sep_list:
                res.append(int(sep))
        
        return res

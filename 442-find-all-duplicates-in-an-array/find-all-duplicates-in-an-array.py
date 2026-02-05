class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        tmp = set()
        res = []
        for num in nums:
            if num in tmp:
                res.append(num)
                tmp.remove(num)
            else:
                tmp.add(num)
        
        return res
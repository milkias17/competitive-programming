class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        required = math.floor(len(nums) / 3)
        res = []
        for k, v in counter.items():
            if v > required:
                res.append(k) 
        
        return res
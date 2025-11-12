class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)
        missing = []
        num = 1
        while True:
            if num not in set_arr:
                missing.append(num)
            
            if len(missing) - 1 == k - 1:
                break
            
            num += 1
        
        return missing[k - 1]
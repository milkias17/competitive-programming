class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1

        cur = 0
        total = 0
        for num in nums:
            cur += num
            if cur % k in counter:
                total += counter[cur % k]
            
            counter[cur % k] += 1
        
        return total

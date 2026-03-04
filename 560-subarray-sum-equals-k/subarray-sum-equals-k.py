class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = Counter()
        prefix[0] += 1
        cur = 0
        count = 0

        for num in nums:
            cur += num
            if cur - k in prefix:
                count += prefix[cur - k]

            prefix[cur] += 1
        
        return count

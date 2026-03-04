class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        calls = [0] * len(nums)
        for left, right in requests:
            calls[left] += 1
            if right + 1 < len(calls):
                calls[right + 1] -= 1
        
        cur = 0
        for i, call in enumerate(calls):
            cur += call
            calls[i] = (cur, i)
        
        calls.sort(key=lambda x: x[0])
        nums.sort()
        permutation = [None] * len(nums)
        for i, num in enumerate(nums):
            idx = calls[i][1]
            permutation[idx] = num
        
        cur = 0
        for i, perm in enumerate(permutation):
            cur += perm
            permutation[i] = cur
        
        cur = 0
        for left, right in requests:
            total = permutation[right]
            if left - 1 >= 0:
                total -= permutation[left - 1]
            cur += total
        
        return cur % (10 ** 9 + 7)
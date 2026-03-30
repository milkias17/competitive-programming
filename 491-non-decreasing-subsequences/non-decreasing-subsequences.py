class Solution:
    def backtrack(self, nums, i, curset, powerset):
        if i >= len(nums):
            if len(curset) >= 2:
                powerset.add(tuple(curset))
            return
        
        prev = curset[-1] if curset else float("-inf")
        if nums[i] < prev:
            self.backtrack(nums, i + 1, curset, powerset)
            return
        
        curset.append(nums[i])
        self.backtrack(nums, i + 1, curset, powerset)
        curset.pop()
        tmp = i + 1
        while tmp < len(nums) and nums[tmp] == nums[i]:
            tmp += 1
        self.backtrack(nums, tmp, curset, powerset)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        powerset = set()
        self.backtrack(nums, 0, [], powerset)
        return list(powerset)
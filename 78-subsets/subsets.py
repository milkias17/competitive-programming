class Solution:
    def backtrack(self, nums, i, curset, powerset):
        if i >= len(nums):
            powerset.append(curset.copy())
            return
        
        curset.append(nums[i])
        self.backtrack(nums, i + 1, curset, powerset)
        curset.pop()
        self.backtrack(nums, i + 1, curset, powerset)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        self.backtrack(nums, 0, [], powerset)
        return powerset
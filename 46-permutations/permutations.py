class Solution:
    def backtrack(self, n, nums, curset, powerset):
        if len(curset) == n:
            powerset.append(curset.copy())
            return
        
        for i, num in enumerate(nums):
            n_nums = nums.copy()
            n_nums.pop(i)
            curset.append(num)
            self.backtrack(n, n_nums, curset, powerset)
            curset.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        self.backtrack(len(nums), nums, [], powerset)
        return powerset
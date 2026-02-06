class Solution:
    def backtrack(self, nums, i,  cur_subset, power_subset):
        if i == len(nums):
            power_subset.append(cur_subset.copy())
            return
        
        cur_subset.append(nums[i])
        self.backtrack(nums, i + 1, cur_subset, power_subset)
        cur_subset.pop()
        self.backtrack(nums, i + 1, cur_subset, power_subset)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, [], res)
        return res
class Solution:
    def backtrack(self, nums, i, cur_set, power_set):
        if i >= len(nums):
            power_set.append(cur_set.copy())
            return
        
        cur_set.append(nums[i])
        self.backtrack(nums, i + 1, cur_set, power_set)
        cur_set.pop()
        self.backtrack(nums, i + 1, cur_set, power_set)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        self.backtrack(nums, 0, [], power_set)
        return power_set
        
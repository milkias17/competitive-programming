class Solution:
    def recurser(self, nums, i, cur_set, power_set):
        if i >= len(nums):
            power_set.append(cur_set.copy())
            return
        
        cur_set.append(nums[i])
        self.recurser(nums, i + 1, cur_set, power_set)

        cur_set.pop()
        self.recurser(nums, i + 1, cur_set, power_set)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur_set, power_set = [], []
        self.recurser(nums, 0, cur_set, power_set)
        return power_set
        
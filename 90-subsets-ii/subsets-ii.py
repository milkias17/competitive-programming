class Solution:
    def recurser(self, nums, i, cur_set, power_set):
        if i >= len(nums):
            power_set.append(cur_set.copy())
            return
        
        cur_set.append(nums[i])
        
        self.recurser(nums, i + 1, cur_set, power_set)
        cur_set.pop()
        tmp = i + 1
        while tmp < len(nums) and nums[tmp] == nums[i]:
            tmp += 1
        self.recurser(nums, tmp, cur_set, power_set)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur_set, power_set = [], []
        self.recurser(sorted(nums), 0, cur_set, power_set)
        return power_set
        
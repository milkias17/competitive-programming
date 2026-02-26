class Solution:
    def backtrack(self, nums, possibilities, cur_set, power_set):
        if len(cur_set) == len(nums):
            power_set.append(cur_set.copy())
            return
        
        for possibility in possibilities:
            cur_set.append(possibility)
            self.backtrack(nums, possibilities - set([possibility]), cur_set, power_set)
            cur_set.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
       power_set = []
       self.backtrack(nums, set(nums), [], power_set)
       return power_set
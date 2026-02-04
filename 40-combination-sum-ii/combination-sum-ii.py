class Solution:
    def backtrack(self, candidates, target, i):
        if self.cur_sum == target:
            self.power_combs.append(self.combs.copy())
            return
        if self.cur_sum > target:
            return
        
        j = i
        while j < len(candidates):
            self.combs.append(candidates[j])
            self.cur_sum += candidates[j]
            self.backtrack(candidates, target, j + 1)
            self.combs.pop()
            self.cur_sum -= candidates[j]
            j += 1
            while j < len(candidates) and candidates[j] == candidates[j - 1]:
                j += 1
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cur_sum = 0
        self.power_combs, self.combs = [], []
        self.backtrack(sorted(candidates), target, 0)
        return self.power_combs
        
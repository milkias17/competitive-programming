class Solution:
    def backtrack(self, candidates, target, i, cur_set, power_set):
        if target == 0:
            power_set.append(cur_set.copy())
            return
        
        if target < 0:
            return
        
        j = i
        while j < len(candidates):
            cur_set.append(candidates[j])
            self.backtrack(candidates, target - candidates[j], j + 1, cur_set, power_set)
            cur_set.pop()
            j += 1
            while j < len(candidates) and candidates[j] == candidates[j - 1]:
                j += 1

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        power_set = []
        self.backtrack(sorted(candidates), target, 0, [], power_set)
        return power_set
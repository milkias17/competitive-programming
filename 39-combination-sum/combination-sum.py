class Solution:
    def recurser(self, candidates, target, cur_combs, cur_sum, power_combs, i):
        if cur_sum == target:
            power_combs.append(cur_combs.copy())
            return
        if cur_sum > target:
            return
        
        for j in range(i, len(candidates)):
            cur_combs.append(candidates[j])
            cur_sum += candidates[j]
            self.recurser(candidates, target, cur_combs, cur_sum, power_combs, j)
            cur_combs.pop()
            cur_sum -= candidates[j]
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        power_combs = []
        self.recurser(candidates, target, [], 0, power_combs, 0)
        return power_combs
        
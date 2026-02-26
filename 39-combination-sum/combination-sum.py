class Solution:
    def backtrack(self, candidates, target, i, cur_set, powerset):
        if sum(cur_set) == target:
            powerset.append(cur_set.copy())
            return

        if sum(cur_set) > target or i >= len(candidates):
            return

        for j in range(i, len(candidates)):
            cur_set.append(candidates[j])
            self.backtrack(candidates, target, j, cur_set, powerset)
            cur_set.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        powerset = []
        self.backtrack(candidates, target, 0, [], powerset)
        return powerset

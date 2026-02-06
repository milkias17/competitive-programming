class Solution:
    def backtrack(self, candidates, target, i, cur_path, res):
        if target == 0:
            res.append(cur_path.copy())
            return

        if target < 0:
            return

        if i >= len(candidates):
            return


        for j in range(i, len(candidates)):
            cur_path.append(candidates[j])
            self.backtrack(candidates, target - candidates[j], j, cur_path, res)        
            cur_path.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(candidates, target, 0, [], res)
        return res
        
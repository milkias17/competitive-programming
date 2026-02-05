class Solution:
    def backtrack(self, n, num_opened, num_closed, cur_path, res):
        if num_opened > n or num_closed > n:
            return
        if num_closed > num_opened:
            return
        if num_opened == n and num_closed == n:
            res.append(cur_path.copy())
            return
        
        
        cur_path.append("(")
        self.backtrack(n, num_opened + 1, num_closed, cur_path, res)
        cur_path.pop()
        cur_path.append(")")
        self.backtrack(n, num_opened, num_closed + 1, cur_path, res)
        cur_path.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n, 1, 0, ["("], res)
        final_res = ["".join(cur) for cur in res]
        return final_res
class Solution:
    def get_new_cand(self, curset, chosen, pattern):
        new_cand = []
        for cand in range(1, 10):
            if cand in curset:
                continue

            if pattern == "I" and cand > chosen:
                new_cand.append(cand)
            
            if pattern == "D" and cand < chosen:
                new_cand.append(cand)
        
        return new_cand

    def backtrack(self, pattern, i, candidates, curset, powerset):
        if len(candidates) == 0:
            return

        if i == len(pattern):
            curset.append(candidates[0])
            powerset.append(curset.copy())
            curset.pop()
            return
        
        
        for cand in candidates:
            curset.append(cand)
            new_cand = self.get_new_cand(curset, curset[-1], pattern[i])
            self.backtrack(pattern, i + 1, new_cand, curset, powerset)
            curset.pop()

    def smallestNumber(self, pattern: str) -> str:
        powerset = []
        self.backtrack(pattern, 0, list(i for i in range(1, 10)), [], powerset)
        return "".join(map(str, sorted(powerset)[0]))
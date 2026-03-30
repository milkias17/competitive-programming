from string import ascii_lowercase

class Solution:
    def backtrack(self, n, k, possibilities, curset, powerset):
        if len(powerset) >= k:
            return
        
        if len(curset) == n:
            powerset.append(curset.copy())
            return
        
        for poss in possibilities:
            if curset and curset[-1] == poss:
                continue
            curset.append(poss)
            self.backtrack(n, k, possibilities, curset, powerset)
            curset.pop()

    def getHappyString(self, n: int, k: int) -> str:
        powerset = []
        self.backtrack(n, k, "abc", [], powerset)
        powerset.sort()
        return "".join(powerset[k - 1]) if k - 1 < len(powerset) else ""
        
class Solution:
    def is_valid(self, curset):
        if len(curset) < 2:
            return False
        res = []
        for x in curset:
            tmp = "".join(x)
            res.append(int(tmp))
        for i in range(1, len(res)):
            if res[i - 1] - res[i] != 1:
                return False
        
        return True

    def backtrack(self, s, i, curset, powerset):
        if i >= len(s):
            if self.is_valid(curset):
                powerset.append(curset.copy())
            return
        
        if len(curset) > 2 and int("".join(curset[-3])) - int("".join(curset[-2])) != 1:
            return
        
        if curset:
            curset[-1].append(s[i])
            self.backtrack(s, i + 1, curset, powerset)
            curset[-1].pop()
        
        curset.append(list(s[i]))
        self.backtrack(s, i + 1, curset, powerset)
        curset.pop()


    def splitString(self, s: str) -> bool:
        powerset = []
        self.backtrack(s, 0, [], powerset)
        return bool(len(powerset))
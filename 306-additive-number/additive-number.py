class Solution:
    def backtrack(self, num, i, curset):
        if i >= len(num):
            return len(curset) >= 3
        
        
        cur = ""
        for j in range (i, len(num)):
            cur += num[j]
            digit = int(cur)

            if j > i and num[i] == "0":
                break

            if len(curset) >= 2:
                expected = curset[-1] + curset[-2]

                if digit < expected:
                    continue
                elif digit > expected:
                    break
            
            curset.append(int(cur))
            if self.backtrack(num, j + 1, curset):
                return True
            curset.pop()
        
        return False
            
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtrack(num, 0, [])
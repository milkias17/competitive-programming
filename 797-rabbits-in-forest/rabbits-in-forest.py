class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0

        for k, v in counter.items():
            if k == 0:
                res += v
                continue
            
            if v <= k + 1:
                res += k + 1
                continue

            groups = (v) // (k + 1)
            res += (k + 1) * groups

            if v % (k + 1) != 0:
                res += k + 1
        
        return res
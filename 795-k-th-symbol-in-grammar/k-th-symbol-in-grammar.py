class Solution:
    def build_grammar(self, n):
        res = [0]        

        while n >= 0:
            new_arr = []
            for num in res:
                if num == 0:
                    new_arr.append(0)
                    new_arr.append(1)
                else:
                    new_arr.append(1)
                    new_arr.append(0)
            res = new_arr
            n -= 1
        
        return res

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prev_idx = (k - 1) // 2
        parity = (k - 1) % 2
        prev_val = self.kthGrammar(n - 1, prev_idx + 1)

        if prev_val == 0:
            if parity == 0:
                return 0
            else:
                return 1
        else:
            if parity == 0:
                return 1
            else:
                return 0


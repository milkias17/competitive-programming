class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prev_idx = (k - 1) // 2
        parity = (k - 1) % 2
        prev_val = self.kthGrammar(n - 1, prev_idx + 1)

        if prev_val == 0:
            return parity
        else:
            return 0 if parity else 1


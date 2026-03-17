class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        tmp = self.myPow(x, abs(n) // 2)
        res = tmp * tmp
        if n % 2 != 0:
            res *= x
        
        return res if n >= 0 else 1 / res
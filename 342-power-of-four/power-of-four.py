class Solution:
    def recurser(self, cur, n):
        if 4 ** cur > n:
            return False
        
        if 4 ** cur == n:
            return True
        
        return self.recurser(cur + 1, n)

    def isPowerOfFour(self, n: int) -> bool:
        return self.recurser(0, n)
        
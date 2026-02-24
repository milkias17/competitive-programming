import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.floor(math.sqrt(c))

        while left <= right:
            cur = left ** 2 + right ** 2
            if cur == c:
                return True
            
            if cur > c:
                right -= 1
            else:
                left += 1
        
        return False
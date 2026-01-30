class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        cur = 2
        for i in range(2, (n * 2 + 1), 2):
            if i % n == 0:
                return i 
        
import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        num_even = (n + 1) // 2
        num_odd = n // 2
        mod = 10**9 + 7

        count =  pow(5, num_even, mod)
        count *= pow(4, num_odd, mod)

        return count % mod
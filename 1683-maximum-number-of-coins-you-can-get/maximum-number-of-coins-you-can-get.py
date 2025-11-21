class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        while len(piles) > 0:
            alice = piles.pop()
            me = piles.pop()
            bob = piles.pop(0)
            count += me
                    
        return count
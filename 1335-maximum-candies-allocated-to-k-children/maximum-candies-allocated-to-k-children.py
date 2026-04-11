class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = max(candies) + 1

        while left + 1 < right:
            mid = (left + right) // 2

            count = 0
            for el in candies:
                count += el // mid
            
            if count >= k:
                left = mid
            else:
                right = mid
        
        return left
        

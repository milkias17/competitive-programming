class Solution:
    def isGood(self, weights, days, ship):
        i = 0
        while days > 0 and i < len(weights):
            cur = 0
            while i < len(weights) and cur + weights[i] <= ship:
                cur += weights[i]
                i += 1
            days -= 1
        
        return i >= len(weights)

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = sum(weights) + 1

        while left + 1 < right:
            mid = (left + right) // 2

            if self.isGood(weights, days, mid):
                right = mid
            else:
                left = mid
        
        return right
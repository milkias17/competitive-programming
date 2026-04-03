class Solution:
    def isGood(self, houses, heaters, radius):
        start = 0
        for heater in heaters:
            low = heater - radius
            high = heater + radius

            while start < len(houses) and low <= houses[start] <= high:
                start += 1
            
            if start >= len(houses):
                return True

        return start >= len(houses)

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        left = -1
        right = max(houses) + max(heaters)

        while left + 1 < right:
            mid = left + (right - left) // 2

            if self.isGood(houses, heaters, mid):
                right = mid
            else:
                left = mid
        
        return right

        
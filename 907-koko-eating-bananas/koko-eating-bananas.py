class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        mid = None
        res = None
        while left <= right:
            mid = left + (right - left) // 2
            tmp_hours = 0
            for num in piles:
                if num <= mid:
                    tmp_hours += 1
                else:
                    tmp_hours += num // mid
                    if num % mid != 0:
                        tmp_hours += 1
            if tmp_hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return res


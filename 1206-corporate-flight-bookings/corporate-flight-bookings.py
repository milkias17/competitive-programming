class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n

        for first, last, seats in bookings:
            prefix[first - 1] += seats
            if last < n:
                prefix[last] -= seats
        
        cur = 0
        for i, num in enumerate(prefix):
            cur += num
            prefix[i] = cur
        
        return prefix
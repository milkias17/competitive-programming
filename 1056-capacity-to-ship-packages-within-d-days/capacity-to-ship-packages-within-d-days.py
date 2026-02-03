class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        min_weight = float("inf")
        while low <= high:
            mid = low + (high - low) // 2
            cur_days = 0
            cur_sum = 0
            for package in weights:
                if cur_sum + package > mid:
                    cur_days += 1
                    cur_sum =0
                cur_sum += package
            cur_days += 1
            
            if cur_days <= days:
                min_weight = min(min_weight, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return min_weight


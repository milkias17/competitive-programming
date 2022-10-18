class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = 0
        window_left = 0
        window_right = 0

        while window_right < k:
            cur_sum += arr[window_right]
            window_right += 1
        
        if (cur_sum / k) >= threshold:
            count += 1
        
        window_right -= 1
        while window_right < len(arr):
            window_right += 1
            if (window_right >= len(arr)):
                break
            cur_sum = cur_sum - arr[window_left] + arr[window_right]
            window_left += 1
            if (cur_sum / k) >= threshold:
                count += 1
        
        return count

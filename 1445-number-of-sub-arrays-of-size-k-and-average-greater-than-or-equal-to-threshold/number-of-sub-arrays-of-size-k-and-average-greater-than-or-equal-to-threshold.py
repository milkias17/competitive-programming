class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        cur_sum = 0
        count = 0

        for right in range(len(arr)):
            cur_sum += arr[right]
            if right - left + 1 < k:
                continue
            
            if (cur_sum / k) >= threshold:
                count += 1

            cur_sum -= arr[left]
            left += 1
        
        return count
        

            

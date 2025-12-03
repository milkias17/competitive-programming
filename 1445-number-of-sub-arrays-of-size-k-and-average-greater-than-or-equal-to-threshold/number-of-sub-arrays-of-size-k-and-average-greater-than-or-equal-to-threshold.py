class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = 0
        num_valid = 0
        left = 0
        for right in range(len(arr)):
            cur_sum += arr[right]

            if right - left + 1 == k:
                if cur_sum / k >= threshold:
                    num_valid += 1
                cur_sum -= arr[left]
                left += 1
        
        return num_valid
        
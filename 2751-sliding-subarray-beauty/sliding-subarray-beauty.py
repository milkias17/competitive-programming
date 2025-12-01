import heapq
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        freq = [0] * 51
        out = []
        for right in range(len(nums)):
            if nums[right] < 0:
                freq[abs(nums[right])] += 1
            
            if right - left + 1 >= k:
                count = 0
                for i in reversed(range(51)):
                    count += freq[i]
                    if count >= x:
                        out.append(-1 * i)
                        break
                
                if count < x:
                    out.append(0)
                
                if nums[left] < 0:
                    freq[abs(nums[left])] -= 1
                
                left += 1
        
        return out

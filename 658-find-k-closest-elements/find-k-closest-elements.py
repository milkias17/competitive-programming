class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        ans = ()
        min_val = float("inf")
        cur_sum = 0
        for right in range(len(arr)):
            cur_sum += abs(arr[right] - x)
            if right - left + 1 == k:
                if cur_sum > min_val:
                    break
                if cur_sum < min_val:
                    min_val = cur_sum
                    ans = (left, right)
                cur_sum -= abs(arr[left] - x)
                left += 1
        
        return arr[ans[0]:ans[1] + 1]
                

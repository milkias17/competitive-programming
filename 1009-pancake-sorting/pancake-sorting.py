class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
    def pancakeSort(self, arr: List[int]) -> List[int]:
        right = len(arr) - 1
        res = []
        while right >= 0:
            max_idx = 0
            for i in range(right + 1):
                if arr[i] > arr[max_idx]:
                    max_idx = i
            
            if max_idx == right:
                right -= 1
            else:
                res.append(max_idx + 1)
                self.reverse(arr, 0, max_idx)
                res.append(right + 1)
                self.reverse(arr, 0, right)
                right -= 1
        
        return res
            



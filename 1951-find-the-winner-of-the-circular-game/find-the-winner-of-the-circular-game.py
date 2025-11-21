class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n + 1)]
        cur = 0
        
        while len(arr) > 1:
            cur += k - 1
            if cur >= len(arr):
                cur = cur % len(arr)
            
            arr.pop(cur)
        
        return arr[0]
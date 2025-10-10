import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        if len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        length = m * n
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            row = math.ceil((mid + 1) / n) - 1
            col = mid - (row * n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
            
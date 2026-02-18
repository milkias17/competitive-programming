class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = 0
        col = len(grid[0]) - 1
        count = 0

        while row < len(grid):
            while col >= 0 and grid[row][col] < 0:
                col -= 1
            
            count += len(grid[0]) - 1 - col
            row += 1
        
        return count
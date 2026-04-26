class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        colors = [[0 for i in range(cols)] for i in range(rows)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col, parent, color):
            colors[row][col] = 1

            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy

                if min(n_row, n_col) < 0 or n_row >= rows or n_col >= cols or (n_row, n_col) == parent or grid[n_row][n_col] != color or colors[n_row][n_col] == 2:
                    continue
                
                if colors[n_row][n_col] == 1:
                    return True
                
                if dfs(n_row, n_col, (row, col), color):
                    return True
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                if colors[i][j] != 0:
                    continue
                if dfs(i, j, None, grid[i][j]):
                    return True
        
        return False

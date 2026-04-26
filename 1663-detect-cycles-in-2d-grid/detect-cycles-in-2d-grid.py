class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def dfs(color, row, col, parent, visited):

            visited.add((row, col))
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy

                if min(n_row, n_col) < 0 or n_row >= rows or n_col >= cols or (n_row, n_col) == parent or grid[n_row][n_col] != color:
                    continue
                
                if (n_row, n_col) in visited:
                    return True
                
                if dfs(color, n_row, n_col, (row, col), visited):
                    return True
            
            return False
        
        colors = set()

        for i in range(rows):
            for j in range(cols):
                colors.add(grid[i][j])
        
        for color in colors:
            visited = set()
            for i in range(rows):
                for j in range(cols):
                    if (i, j) in visited or grid[i][j] != color:
                        continue
                    
                    if dfs(color, i, j, None, visited):
                        return True
        
        return False




                


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_cells = set()
        a_cells = set()

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if min(n_row, n_col) < 0 or n_row >= len(heights) or n_col >= len(heights[0]) or heights[row][col] > heights[n_row][n_col]:
                    continue
                
                dfs(n_row, n_col, visited)
        
        for i in range(len(heights[0])):
            dfs(0, i, p_cells)
        
        for i in range(len(heights)):
            dfs(i, 0, p_cells)
        
        for i in range(len(heights[0])):
            dfs(len(heights) - 1, i, a_cells)
        
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, a_cells)
        
        return list(a_cells.intersection(p_cells))
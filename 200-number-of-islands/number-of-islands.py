class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if min(row, col) < 0 or row >= rows or col >= cols or (row, col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row, col))
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                dfs(n_row, n_col)
        

        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited or grid[i][j] == "0":
                    continue
                count += 1
                dfs(i, j)
        
        return count
            
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if min(i, j) < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            perimeter = dfs(i, j + 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i - 1, j)
            perimeter += dfs(i, j - 1)

            return perimeter
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    return dfs(i, j)
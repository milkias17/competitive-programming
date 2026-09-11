class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if grid[r][c] != 1:
                return 0
            
            area = 1
            visited.add((r, c))
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if min(nr, nc) >= 0 and nr < rows and nc < cols and (nr, nc) not in visited:
                    area += dfs(nr, nc)
            
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
            

        return max_area
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c, health):
            if r == rows - 1 and c == cols - 1:
                return True
            
            visited.add((r, c, health))
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if min(nr, nc) < 0 or nr >= rows or nc >= cols:
                    continue

                n_health = health
                if grid[nr][nc] == 1:
                    n_health -= 1
                
                if n_health < 1 or (nr, nc, n_health) in visited:
                    continue

                if dfs(nr, nc, n_health):
                    return True
            
            return False
        
        return dfs(0, 0, health - grid[0][0])

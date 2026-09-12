class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1
        
        def check_valid(r, c):
            return min(r, c) >= 0 and r < rows and c < cols and (r, c) not in visited and grid[r][c] == 1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minutes = 0
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy

                    if check_valid(nr, nc):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        fresh_count -= 1
            
            minutes += 1
        
        if fresh_count > 0:
            return -1
        
        return minutes


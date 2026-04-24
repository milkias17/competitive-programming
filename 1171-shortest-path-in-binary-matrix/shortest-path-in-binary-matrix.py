class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        n = len(grid)

        queue = deque()
        if grid[0][0] == 0:
            queue.append((0, 0))

        found = False
        height = 1

        visited = set([(0, 0)])

        while queue and not found:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return height
                    
                for dx, dy in directions:
                    n_r, n_c = r + dx, c + dy
                    if (n_r, n_c) not in visited and min(n_r, n_c) >= 0 and n_r < n and n_c < n and grid[n_r][n_c] == 0:
                        visited.add((n_r, n_c))
                        queue.append((n_r, n_c))

                
            height += 1
        
        return -1
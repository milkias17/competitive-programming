class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()

        def dfs(row, col, visited):
            visited.add((row, col))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            for dx, dy in directions:
                r, c = row + dx, col + dy
                
                if (r < 0 or r >= rows or 
                    c < 0 or c >= cols or 
                    (r, c) in visited or 
                    heights[r][c] < heights[row][col]):
                    continue
                
                dfs(r, c, visited)

        for i in range(rows):
            dfs(i, 0, p_visited)
        for j in range(cols):
            dfs(0, j, p_visited)

        for i in range(rows):
            dfs(i, cols - 1, a_visited)
        for j in range(cols):
            dfs(rows - 1, j, a_visited)

        out = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in p_visited and (i, j) in a_visited:
                    out.append([i, j])

        return out


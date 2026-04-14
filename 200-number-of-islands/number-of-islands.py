class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(i, j):
            if (
                (i, j) in visited
                or min(i, j) < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or grid[i][j] == "0"
            ):
                return

            visited.add((i, j))
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        count = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "0" or (i, j) in visited:
                    continue
                count += 1
                dfs(i, j)

        return count
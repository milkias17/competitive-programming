class Solution: 
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = [[[-2 for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, k):
            if row >= rows or col >= cols:
                return -1

            score = grid[row][col]
            cost = score if score != 2 else 1

            if k - cost < 0:
                return -1

            if row == rows - 1 and col == cols - 1:
                return score

            if memo[row][col][k] != -2:
                return memo[row][col][k]

            res = max(
                dfs(row, col + 1, k - cost), dfs(row + 1, col, k - cost)
            )
            memo[row][col][k] = res + score if res != -1 else res
            return memo[row][col][k]

        return dfs(0, 0, k)
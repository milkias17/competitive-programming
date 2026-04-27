class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        need_next = {
            1: set([3, 5]),
            2: set([5, 6]),
            3: set([5, 6, 2]),
            4: set([5, 6, 2]),
            5: set([1, 3, 4]),
            6: set([1, 3, 5])
        }

        direction_street = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col, prev):
            visited.add((row, col))
            street = grid[row][col]
            flag = prev is None
            for dx, dy in direction_street[street]:
                n_row, n_col = row + dx, col + dy
                if min(n_row, n_col) < 0 or n_row >= rows or n_col >= cols:
                    continue
                if prev == (n_row, n_col):
                    flag = True

            if not flag:
                return False

            if row == rows - 1 and col == cols - 1:
                return True
                
            for dx, dy in direction_street[street]:
                n_row, n_col = row + dx, col + dy
                if min(n_row, n_col) < 0 or n_row >= rows or n_col >= cols or (n_row, n_col) in visited:
                    continue
                if dfs(n_row, n_col, (row, col)):
                    return True
                
            return False
        
        return dfs(0, 0, None)

            
        

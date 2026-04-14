class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    num_fresh += 1

        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        count = 0
        minutes = 0
        while queue:
            row, col, height = queue.popleft()
            visited.add((row, col))
            minutes = max(minutes, height)

            for dx, dy in neighbors:
                n_row, n_col = row + dx, col + dy
                if (
                    min(n_row, n_col) >= 0
                    and n_row < rows
                    and n_col < cols
                    and (n_row, n_col) not in visited
                    and grid[row][col] == 1
                ):
                    queue.append((row, col, height + 1))

            if grid[row][col] == 1:
                count += 1

        if count != num_fresh:
            print(num_fresh, count)
            return -1
        
        return minutes
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    num_fresh += 1

        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        count = 0
        minutes = 0
        while queue:
            row, col, height = queue.popleft()
            # print(f"Checking {row}, {col}, {height}")
            visited.add((row, col))
            minutes = max(minutes, height)

            for dx, dy in neighbors:
                n_row, n_col = row + dx, col + dy
                if (
                    min(n_row, n_col) >= 0
                    and n_row < rows
                    and n_col < cols
                    and (n_row, n_col) not in visited
                    and grid[n_row][n_col] == 1
                ):
                    queue.append((n_row, n_col, height + 1))
                    visited.add((n_row, n_col))

            if grid[row][col] == 1:
                count += 1

        # print(f"Minutes: {minutes}")
        if count != num_fresh:
            # print(f"Wrong count: {count} != {num_fresh}")
            return -1

        return minutes
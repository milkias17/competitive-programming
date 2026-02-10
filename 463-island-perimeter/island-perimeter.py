class Solution:
    def _neighbors(self, row, col):
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        return [(row + d_row, col + d_col) for d_row, d_col in neighbors]

    def dfs(self, grid, row, col, visited):
        if (row, col) in visited:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])

        if min(row, col) < 0 or row >= num_rows or col >= num_cols:
            return 0

        visited.add((row, col))
        count = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for d_row, d_col in neighbors:
            new_row, new_col = row + d_row, col + d_col
            if new_row < 0 or new_row >= num_rows:
                count += 1
            if new_col < 0 or new_col >= num_cols:
                count += 1
            count += self.dfs(grid, new_row, new_col, visited)

        visited.remove((row, col))
        return count

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.append((0, 0))
        perimeter = 0
        visited = set()
        visited.add((0, 0))
        num_rows, num_cols = len(grid), len(grid[0])

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                    continue
                neighbors = self._neighbors(row, col)

                if grid[row][col] == 0:
                    for new_row, new_col in neighbors:
                        if (new_row, new_col) not in visited:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
                    continue

                for new_row, new_col in self._neighbors(row, col):
                    if new_row < 0:
                        perimeter += 1
                    if new_row >= num_rows:
                        perimeter += 1
                    if new_col < 0:
                        perimeter += 1
                    if new_col >= num_cols:
                        perimeter += 1

                    if (
                        new_row >= 0
                        and new_row < num_rows
                        and new_col >= 0
                        and new_col < num_cols
                        and grid[new_row][new_col] == 0
                    ):
                        perimeter += 1

                    if (new_row, new_col) in visited:
                        continue

                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        return perimeter
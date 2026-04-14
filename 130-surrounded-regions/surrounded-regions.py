class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visisted = set()
        rows, cols = len(board), len(board[0])

        def not_valid(row, col):
            return row >= rows or col >= cols or row < 0 or col < 0

        def dfs(row, col, region):
            if not_valid(row, col):
                return False

            region.add((row, col))
            visisted.add((row, col))
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if (n_row, n_col) in region or not_valid(n_row, n_col) or board[n_row][n_col] == "X":
                    continue

                if not dfs(n_row, n_col, region):
                    return False

            return True

        for i in range(rows):
            for j in range(cols):
                if (i, j) in visisted or board[i][j] == "X":
                    continue

                region = set()
                res = dfs(i, j, region)
                if not res:
                    continue

                for row, col in region:
                    board[row][col] = "X"
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])

        def not_valid(row, col):
            return row >= rows or col >= cols or row < 0 or col < 0

        def dfs(row, col, region):
            if not_valid(row, col):
                return False

            region.add((row, col))
            visited.add((row, col))
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if (n_row, n_col) in region or (
                    not not_valid(n_row, n_col) and board[n_row][n_col] == "X"
                ):
                    continue

                if not dfs(n_row, n_col, region):
                    return False

            return True

        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited or board[i][j] == "X":
                    continue

                region = set()
                res = dfs(i, j, region)
                if not res:
                    continue

                for row, col in region:
                    board[row][col] = "X"
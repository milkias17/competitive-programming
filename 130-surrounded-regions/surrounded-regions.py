class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(row, col, to):
            if min(row, col) < 0 or row >= rows or col >= cols or (row, col) in visited or board[row][col] == "X":
                return
            
            visited.add((row, col))
            board[row][col] = to
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                dfs(n_row, n_col, to)


        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    dfs(i, j, "C")
        
        visited.clear()
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and board[i][j] == "O":
                    dfs(i, j, "X")
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "C":
                    board[i][j] = "O"
        

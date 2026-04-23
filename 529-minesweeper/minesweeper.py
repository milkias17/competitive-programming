class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])

        def dfs(row, col, visited):
            if board[row][col] == "M":
                return
                
            visited.add((row, col))
            directions = [[1,0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

            mines = 0
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if min(n_row, n_col) < 0 or n_row >= rows or n_col >= cols:
                    continue
                if board[n_row][n_col] == "M":
                    mines += 1
            
            if mines != 0:
                board[row][col] = str(mines)
                return

            board[row][col] = "B"
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if min(n_row, n_col) < 0 or n_row >= rows or n_col >= cols:
                    continue
                
                if (n_row, n_col) not in visited:
                    dfs(n_row, n_col, visited)
            
        r, c = click
        selected = board[r][c]
        if selected == "M":
            board[r][c] = "X"
            return board
        
        visited = set()
        dfs(r, c, visited)

        return board
        

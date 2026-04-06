from collections import defaultdict
from typing import List


class Solution:
    def backtrack(self, board, row, col, row_opts, col_opts, grid_opts, count):
        if count == len(self.empty):
            return True

        num_rows, num_cols = len(board), len(board[0])
        if row >= num_rows:
            return False

        n_row = row
        n_col = col + 1

        if n_col >= num_cols:
            n_row = row + 1
            n_col = 0

        if board[row][col] != ".":
            return self.backtrack(board, n_row, n_col, row_opts, col_opts, grid_opts, count)
        else:
            g_key = (row // 3, col // 3)
            col_poss = col_opts[col]
            row_poss = row_opts[row]
            grid_poss = grid_opts[g_key]
            options = row_poss.intersection(col_poss, grid_poss)

            for option in options:
                board[row][col] = option

                row_opts[row].discard(option)
                col_opts[col].discard(option)
                grid_opts[g_key].discard(option)
                if self.backtrack(
                    board, n_row, n_col, row_opts, col_opts, grid_opts, count + 1
                ):
                    return True

                board[row][col] = "."
                row_opts[row].add(option)
                col_opts[col].add(option)
                grid_opts[g_key].add(option)

            return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_poss = defaultdict(lambda: set(str(i) for i in range(1, 10)))
        col_poss = defaultdict(lambda: set(str(i) for i in range(1, 10)))
        grid_poss = defaultdict(lambda: set(str(i) for i in range(1, 10)))
        self.empty = set()

        for i, row in enumerate(board):
            tmp = set()
            for col, val in enumerate(row):
                if val == ".":
                    self.empty.add((i, col))
                    continue
                tmp.add(val)
                col_poss[col].discard(val)

                g_row = i // 3
                g_col = col // 3
                grid_poss[(g_row, g_col)].discard(val)

            row_poss[i] -= tmp

        print(f"org count: {len(self.empty)}")
        self.backtrack(board, 0, 0, row_poss, col_poss, grid_poss, 0)

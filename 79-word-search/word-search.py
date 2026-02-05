from typing import List


class Solution:
    def recurser(self, board, row, col, i, word, used):
        if i >= len(word):
            return True

        if (row, col) in used:
            return False

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] == word[i]:
            tmp = used.copy()
            tmp.append((row, col))
            adjacent_row_cols = [
                (row, col - 1),
                (row, col + 1),
                (row - 1, col),
                (row + 1, col),
            ]
            for adj_row, adj_col in adjacent_row_cols:
                res = self.recurser(board, adj_row, adj_col, i + 1, word, tmp)
                if res:
                    return True

        if i == 0:
            if col + 1 < len(board[0]):
                return self.recurser(board, row, col + 1, i, word, used)
            else:
                return self.recurser(board, row + 1, 0, i, word, used)
        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.recurser(board, 0, 0, 0, word, [])

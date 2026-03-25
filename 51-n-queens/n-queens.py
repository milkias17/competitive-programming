class Solution:
    def add_attackables(self, n, row, col):
        disallowed = set()
        disallowed.add((row, col))
        for i in range(n):
            disallowed.add((i, col))
            disallowed.add((row, i))

        for i in range(1, n):
            if row - i >= 0 and col - i >= 0:
                disallowed.add((row - i, col - i))
            if row + i < n and col + i < n:
                disallowed.add((row + i, col + i))
            if row + i < n and col - i >= 0:
                disallowed.add((row + i, col - i))
            if row - i >= 0 and col + i < n:
                disallowed.add((row - i, col + i))
        return disallowed

    def backtrack(self, n, row, col, disallowed, curset, powerset):
        if len(curset) == n:
            powerset.append(curset.copy())
            return

        n_row = None
        n_col = None
        if col + 1 >= n:
            n_row = row + 1
            n_col = 0
        else:
            n_row = row
            n_col = col + 1

        if row >= n or col >= n:
            return

        if (row, col) in disallowed:
            self.backtrack(n, n_row, n_col, disallowed, curset, powerset)
            return

        curset.add((row, col))

        tmp = self.add_attackables(n, row, col)

        self.backtrack(n, n_row, n_col, disallowed.union(tmp), curset, powerset)
        curset.discard((row, col))
        self.backtrack(n, n_row, n_col, disallowed, curset, powerset)

    def solveNQueens(self, n: int) -> List[List[str]]:
        powerset = []
        self.backtrack(n, 0, 0, set(), set(), powerset)
        res = []
        for ans in powerset:
            board = []
            for r in range(n):
                row = []
                for c in range(n):
                    if (r, c) in ans:
                        row.append("Q")
                    else:
                        row.append(".")
                board.append("".join(row))
            res.append(board)

        return res

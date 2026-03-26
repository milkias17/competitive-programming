class Solution:
    def attacks(self, n, row, col):
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
        if row >= n:
            if len(curset) == n:
                powerset.append(curset.copy())
            return
        
        n_row = row
        n_col = col + 1

        if n_col >= n:
            n_row = row + 1
            n_col = 0
        
        if (row, col) in disallowed:
            self.backtrack(n, n_row, n_col, disallowed, curset, powerset)
            return
        
        curset.append((row, col))
        tmp = self.attacks(n, row, col)
        self.backtrack(n, n_row, n_col, disallowed.union(tmp), curset, powerset)
        curset.pop()
        self.backtrack(n, n_row, n_col, disallowed, curset, powerset)

    def totalNQueens(self, n: int) -> int:
        powerset = []
        self.backtrack(n, 0, 0, set(), [], powerset)
        return len(powerset)

        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        cols = set()
        rows = set()

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    rows.add(i)
                    cols.add(j)

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in rows or j in cols:
                    matrix[i][j] = 0
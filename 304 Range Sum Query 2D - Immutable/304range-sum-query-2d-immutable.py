class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = []

        for row in range(0, len(matrix)):
            new_col = []
            new_col.append(matrix[row][0])
            for i in range(1, len(matrix[row])):
                new_col.append(new_col[i - 1] + matrix[row][i])
            self.prefix_matrix.append(new_col)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            if col1 > 0:
                sum += self.prefix_matrix[i][col2] - self.prefix_matrix[i][col1 - 1]
            else:
                sum += self.prefix_matrix[i][col2]

        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
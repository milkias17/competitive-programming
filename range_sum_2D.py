from typing import List

"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined
by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
NumMatrix(int[][] matrix) Initializes the object with the integer matrix
matrix.  int sumRegion(int row1, int col1, int row2, int col2) Returns the
sum of the elements of matrix inside the rectangle defined by its upper
left corner (row1, col1) and lower right corner (row2, col2).  You must
design an algorithm where sumRegion works on O(1) time complexity.
"""


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


if __name__ == "__main__":
    obj = NumMatrix([[-1]])
    print(obj.sumRegion(0, 0, 0, 0))

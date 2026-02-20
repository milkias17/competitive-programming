class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        row, col = 0, 0

        while row >= 0 and row < len(mat) and col >= 0 and col < len(mat[0]):
            while row >= 0 and col < len(mat[0]):
                res.append(mat[row][col])
                row -= 1
                col += 1
            
            row += 1
            col -= 1
            if col + 1 < len(mat[0]):
                col += 1
            else:
                row += 1
            
            while row < len(mat) and col >= 0:
                res.append(mat[row][col])
                row += 1
                col -= 1
            
            row -= 1
            col += 1
            if row + 1 < len(mat):
                row += 1
            else:
                col += 1
        
        return res

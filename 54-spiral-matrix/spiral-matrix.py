class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = set()
        cols = set()

        next_dir = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }

        row, col = 0, 0
        ptr = (0, 1)
        res = []
        not_valid = lambda row, col: row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or row in rows or col in cols
        while row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
            res.append(matrix[row][col])
            row += ptr[0]
            col += ptr[1]
            if not_valid(row, col):
                row -= ptr[0]
                col -= ptr[1]
                if ptr[0] != 0:
                    cols.add(col)
                elif ptr[1] != 0:
                    rows.add(row)

                ptr = next_dir[ptr]
                if (ptr[0] != 0 and row + ptr[0] in rows) or (ptr[1] != 0 and col + ptr[1] in cols):
                    break
                row += ptr[0]
                col += ptr[1]
        
        return res



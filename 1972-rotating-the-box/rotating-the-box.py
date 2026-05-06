class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])
        new_box = [["." for _ in range(rows)] for _ in range(cols)]

        for i in range(rows - 1, -1, -1):
            last_open_row = len(new_box) - 1
            col = rows - 1 - i
            for j in range(cols - 1, -1, -1):
                cur = boxGrid[i][j]
                if cur == ".":
                    continue
                if cur == "#":
                    new_box[last_open_row][col] = cur
                    last_open_row -= 1
                elif cur == "*":
                    new_box[j][col] = "*"
                    last_open_row = j - 1
        
        return new_box
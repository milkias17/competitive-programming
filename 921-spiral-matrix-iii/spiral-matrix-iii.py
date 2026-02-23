class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        k = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cur_direction = 0
        res = [[rStart, cStart]]
        while len(res) < rows * cols:
            if cur_direction == 0 or cur_direction == 2:
                k += 1

            for i in range(k):
                rStart += directions[cur_direction][0]
                cStart += directions[cur_direction][1]
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    res.append([rStart, cStart])

                    if len(res) == rows * cols:
                        return res

                
            cur_direction = (cur_direction + 1) % 4
        
        return res



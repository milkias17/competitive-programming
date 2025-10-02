class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col_dict = dict()
        box_dict = dict()
        for row_n, row in enumerate(board):
            row_s = set()
            for col_n, el in enumerate(row):
                if el == ".":
                    continue
                
                if el in row_s:
                    # print("false by row")
                    return False
                else:
                    row_s.add(el)
                
                if col_n not in col_dict:
                    col_dict[col_n] = {el}
                elif el in col_dict[col_n]:
                    # print("false by col: ", el, row_n, col_n)
                    return False
                else:
                    col_dict[col_n].add(el)
                
                b_row , b_col = 0, 0
                if (row_n + 1) < 4:
                    b_row = 1
                elif (row_n + 1) < 7:
                    b_row = 2
                else:
                    b_row = 3
                
                if col_n + 1 < 4:
                    b_col = 1
                elif col_n + 1 < 7:
                    b_col = 2
                else:
                    b_col = 3
                
                box_n = "{}{}".format(b_row, b_col)
                if box_n not in box_dict:
                    box_dict[box_n] = {el}
                elif el in box_dict[box_n]:
                    # print(b_row, b_col)
                    # print("Row: {}, Col: {}, Box_n: {}, El: {}".format(row_n, col_n, box_n, el), box_dict[box_n])
                    return False
                else:
                    box_dict[box_n].add(el)

        return True           
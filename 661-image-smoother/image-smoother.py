class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        new_img = []
        num_row, num_col = len(img), len(img[0])
        for i, row in enumerate(img):
            new_row = []
            for j, col in enumerate(row):
                sum_val = 0
                count = 0
                for d_row, d_col in neighbors:
                    tmp_row, tmp_col = i + d_row, j + d_col
                    if tmp_row < 0 or tmp_row >= num_row or tmp_col < 0 or tmp_col >= num_col:
                        continue
                    
                    sum_val += img[tmp_row][tmp_col]
                    count += 1
                
                sum_val += img[i][j]
                count += 1
                new_row.append(math.floor(sum_val / count))
            
            new_img.append(new_row)
        
        return new_img
                    


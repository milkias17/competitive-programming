class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_img = []
        for row in image:
            new_row = list(reversed(row))
            for i in range(len(new_row)):
                new_row[i] = new_row[i] ^ 1
            new_img.append(new_row)
        
        return new_img

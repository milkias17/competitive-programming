class Solution:
    def dfs(self, image, sr, sc, color, org):
        max_row, max_col = len(image), len(image[0])
        if min(sr, sc) < 0 or sr >= max_row or sc >= max_col:
            return
        if image[sr][sc] != org:
            return
        if image[sr][sc] == color:
            return
        
        image[sr][sc] = color
        neighbors = [[1,0], [-1,0], [0, 1], [0, -1]]
        for d_row, d_col in neighbors:
            new_row, new_col = sr + d_row, sc + d_col
            self.dfs(image, new_row, new_col, color, org)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, color, image[sr][sc])
        return image
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            for i, row in enumerate(mat):
                for j in range(i + 1, len(row)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for i, row in enumerate(mat):
                for j in range(len(row) // 2):
                    mat[i][j], mat[i][len(row) - 1 - j] = mat[i][len(row) - 1 - j], mat[i][j]
            
            flag = True
            for i, row in enumerate(mat):
                for j, el in enumerate(row):
                    if el != target[i][j]:
                        flag = False
                        break

            if flag:
                return True

        return False
            
        



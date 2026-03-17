class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows == 1:
            return triangle

        triangle.append([1,1])

        for i in range(3, numRows + 1):
            cur = [1] * i
            tmp = triangle[-1]
            for j in range(1, i - 1):
                cur[j] = tmp[j - 1] + tmp[j]
            triangle.append(cur)
        
        return triangle
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col = [0]*m
        row = [0]*n

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    col[j] = 1
                    row[i] = 1
        for i in range(n):
            for j in range(m):
                if col[j] or row[i]:
                    matrix[i][j] =0
        
        
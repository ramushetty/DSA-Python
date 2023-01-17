class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])

        row = [1] * R
        column = [1] * C
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    row[i] = 0
                    column[j] = 0
        for i in range(R):
            for j in range(C):
                if row[i] == 0 or column[j] == 0:
                    matrix[i][j] = 0

        return 
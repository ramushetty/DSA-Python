class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        temp = [True]*4

        for i in range(n):
            for j in range(n):

                if mat[i][j] != target[i][j]:
                    temp[0] = False
                if mat[i][j] != target[n-j-1][i]:
                    temp[1] = False
                if mat[i][j] != target[n-i-1][n-j-1]:
                    temp[2] = False
                if mat[i][j] != target[j][n-i-1]:
                    temp[3] = False
        return temp[0] or temp[1] or temp[2] or temp[3]
